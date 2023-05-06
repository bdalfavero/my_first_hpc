#!/usr/bin/env python3

import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], index_col="t")
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(
    df['x'], df['y'], df['z']
)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
