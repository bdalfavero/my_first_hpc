#!/usr/bin/env python3

import sys
#import pytomlpp as pt
import json
import numpy as np
from scipy.integrate import solve_ivp
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


def solve_odes(t_final, q0, params, **kwargs):
    """
    solve_odes(t_final, q0, params, **kwargs)

    solves the lorenz system for initial condition 
    q0 = (x0, y0, z0),
    parameters q = (sigma, r, b), and total time t_final.
    **kwargs are passed to scipy.integrate.solve_ivp.
    """

    deriv = lambda t, q: lorenz_deriv(t, q, params)
    sol = solve_ivp(deriv, (0., t_final), q0, **kwargs)

    return sol

# Print a help message, if the user asks.
if "--help" in sys.argv:
    print(
        """
        lorenz.py

        Simulation of a lorenz attractor.

        Format for interface:
        lorenz.py <input file> <output file>
        The input file is a TOML file with the necessary data. 
        See the repo for more. The ouptut file is a CSV with the solution.
        """
    )
    quit()

# If the user has not provided enough arguments, print a help message.
if len(sys.argv) < 3:
    print(
        """
        lorenz.py <input file> <output file>

        for more help, please run "lorenz.py --help"
        """
    )
    quit()

# Take parameters from the input files.
with open(sys.argv[1]) as fp:
    input_dict = json.load(fp)

# Extract required arguments from the input.
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

# Deal with optional arguments.
if "method" in input_dict["integration"].keys():
    method = input_dict["integration"]["method"]
    assert type(method) == str, "method must be a string."
else:
    method = "RK45"

if "dense_output" in input_dict["integration"].keys():
    dense_output = input_dict["integration"]["dense_output"]
    assert type(dense_output) == bool, "dense_output must be a boolean."
    # If we specify dense output, we must give a number of evaluation points.
    # If this is absent, throw an error. 
    if dense_output:
        assert "points" in input_dict["integration"].keys(), \
            "For dense output, points must be specified."
        num_points = input_dict["integration"]["points"]
        assert type(num_points) == int, "points must be an integer."
else:
    dense_output = False

# Solve the ODE's.
sol = solve_odes(
    t_final, q0, params, 
    method=method, dense_output=dense_output
)

# Either use the computed points for output, or the dense output interpolants.
if dense_output:
    t_out = np.linspace(0.0, t_final, num=num_points)
    y_out = sol.sol(t_out)
else:
    t_out = sol.t
    y_out = sol.y

# Write data to file.
df = pd.DataFrame(y_out.T, index=t_out, columns=["x", "y", "z"])
df.index.name = "t"
df.to_csv(sys.argv[2])
