#!/usr/bin/env python3

import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], index_col="t")
ax = sns.lineplot(
    data=df 
    # x="t", 
    # y=["x", "y", "z"]
)
plt.show()
