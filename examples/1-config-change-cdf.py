import numpy as np
import matplotlib.pyplot as plt
import os

# %% Style
SECONDARY_COLOR = "#808080"
FONT_SIZE_SM = 18
FONT_SIZE_MD = 20
FONT_SIZE_LG = 22
COLORS = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:red",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
]

plt.rcParams.update(
    {
        "figure.figsize": (8, 4.5),
        "font.size": FONT_SIZE_SM,
        "axes.titlesize": FONT_SIZE_LG,
        "axes.labelsize": FONT_SIZE_LG,
        "font.family": "Calibri",
        "legend.framealpha": 0.5,
        "legend.fontsize": FONT_SIZE_SM,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.edgecolor": SECONDARY_COLOR,
        "xtick.color": SECONDARY_COLOR,
        "ytick.color": SECONDARY_COLOR,
        "xtick.labelsize": FONT_SIZE_MD,
        "ytick.labelsize": FONT_SIZE_MD,
        "grid.color": SECONDARY_COLOR,
        "grid.linestyle": ":",
        "grid.linewidth": 1,
        "axes.grid": True,
    }
)

# %% Data
with open(os.path.join(os.path.dirname(__file__), "1-config_change_cdf.txt"), "r") as fp:
    dat = fp.read()
    fp.close()
data = []
for l in dat.splitlines():
    d = l.split(" ")
    data.append((float(d[0]), float(d[1])))


# %% Plot
def plot_cdf(data, xlabel, ylabel):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot([x[0] for x in data], [x[1] for x in data], alpha=0.7)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    plt.tight_layout()
    plt.show()


plot_cdf(data, "Modified config %", "Cumulated probability")
