# Use the following data for this assignment:

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# %matplotlib notebook

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                   np.random.normal(43000, 100000, 3650),
                   np.random.normal(43500, 140000, 3650),
                   np.random.normal(48000, 70000, 3650)],
                  index=[1992, 1993, 1994, 1995])


def plot_df(df):
    years = np.arange(1992, 1996)
    y1 = df.loc[years[0], :]
    y2 = df.loc[years[1], :]
    y3 = df.loc[years[2], :]
    y4 = df.loc[years[3], :]
    Y = [y1, y2, y3, y4]

    fig = plt.figure()
    plt.boxplot(Y, whis='range')


plot_df(df)
# plt.show('hold')
