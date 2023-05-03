#!/usr/bin/env python3

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


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

q0 = np.array([1.0, 0.0, 0.0])
params = np.array([3.0, 2.0, 1.0])
t_final = 10.0
sol = solve_odes(t_final, q0, params)

fig, ax = plt.subplots()
ax.plot(sol.t, sol.y.T)
plt.show()