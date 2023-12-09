import numpy as np
import matplotlib.pyplot as plt

# %% style
SECONDARY_COLOR = "#505050"
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
    "tab:gray', 'tab:olive",
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
        "xtick.labelsize": FONT_SIZE_LG,
        "ytick.labelsize": FONT_SIZE_LG,
        "grid.color": SECONDARY_COLOR,
        "grid.linestyle": ":",
        "grid.linewidth": 1,
        # enable grid
        "axes.grid": True,
        # enable y axis grid only
        "axes.grid.axis": "y",
    }
)
# %% Data
nets = ["A", "B", "C", "D", "E", "F", "G", "H"]
time1data = [3760, 399, 166, 7391, 1043, 448, 1011, 6148]
time2data = [3784, 432, 185, 22131, 40013, 502, 8941, 2143491]

net_labels = ["Net" + n for n in nets]
time1data = [t / 1000 for t in time1data]
time2data = [t / 1000 for t in time2data]


# %% Plot
def plottbl4():
    barWidth = 0.5
    # time2 = time1
    fig, ax = plt.subplots()
    x_axis = np.arange(len(net_labels))
    plt.xticks(x_axis, net_labels, rotation=15)
    ax.bar(x_axis, time1data, width=barWidth, hatch="//", linewidth=1, edgecolor="tab:green", color="none", label="T1")
    ax.bar(
        x_axis,
        [time2data[i] - time1data[i] for i in range(0, 8)],
        bottom=time1data,
        width=barWidth,
        hatch="xx",
        linewidth=2,
        edgecolor="tab:red",
        color="none",
        label="T2",
    )
    ax.legend(draggable=True)

    ax.set_ylabel("Time (s)")
    ax.set_yscale("log")
    plt.tight_layout()
    plt.show()


# fig16 rdg
plottbl4()
