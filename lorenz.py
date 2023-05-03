#!/usr/bin/env python3

import sys
import pytomlpp as pt
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd


def lorenz_deriv(t, q, params):
    """
    deriv(t, q, params)

    Returns derivative of Lorenz system for 
    q = (x, y, z)
    params = (sigma, r, b)
    d/dt x = sigma (y - x)
    d/dt y = -xz + rx - y
    d/dt z = xy - bz
    """

    dq = np.zeros(q.shape)
    dq[0] = params[0] * (q[1] - q[0])
    dq[1] = -q[2] * q[0] + params[1] * q[0] - q[1]
    dq[2] = q[0] * q[1] - params[2] * q[1]

    return dq


def solve_odes(t_final, q0, params):
    """
    solve_odes(t_final, q0, params)

    solves the lorenz system for initial condition 
    q0 = (x0, y0, z0),
    parameters q = (sigma, r, b), and total time t_final.
    """

    deriv = lambda t, q: lorenz_deriv(t, q, params)
    sol = solve_ivp(deriv, (0., t_final), q0, method="RK45")

    return sol

# Take parameters from the input files.
with open(sys.argv[1]) as fp:
    input_dict = pt.load(fp)

q0 = np.array([
    input_dict["initial_conditions"]["x"], 
    input_dict["initial_conditions"]["y"], 
    input_dict["initial_conditions"]["z"]
])
params = np.array([
    input_dict["parameters"]["sigma"], 
    input_dict["parameters"]["r"], 
    input_dict["parameters"]["b"]])
t_final = input_dict["integration"]["t_final"]

# Solve the ODE's.
sol = solve_odes(t_final, q0, params)

# Write data to file.
df = pd.DataFrame(sol.y.T, index=sol.t, columns=["x", "y", "z"])
df.index.name = "t"
df.to_csv(sys.argv[2])