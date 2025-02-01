import matplotlib.pyplot as plt
import numpy as np


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
HATCHS = ["--", "//", "xx", "\\", "oo", "..", "+", "O", "*"]

plt.rcParams.update(
    {
        "figure.figsize": (3.5, 4.5),
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
        # disable x axis grid
        "axes.grid.axis": "y",
    }
)


# %% Data
if __name__ == "__main__":
    x_labels = ["Stm1", "Stm2", "CM"]  # , "Utility", 'Running Time']
    ydata = [
        [1.863, 54.2329, 8.679],
        # [0.1415584416,0.1854256854, 1, 1, 'NetD'],
        # [0.04523809524,0.05428571429, 1, 'NetE'],
        # [0.0582278481,0.05907172996, 1, 'NetF'],
        # [0,0, 1, 'NetG'],
        # [0,0, 1, 'NetH'],
        # [1,1, 1, 'NetI'],
    ]

    # %% Plot
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.grid(True, alpha=0.5)
    for idx in range(0, len(ydata)):
        hdl = ax.bar(
            [i + idx * (0.9 / len(ydata)) for i in range(0, len(x_labels))],
            ydata[idx][0 : len(x_labels)],
            align="center",
            hatch=HATCHS[idx],
            color="none",
            edgecolor=COLORS[idx],
            linewidth=2,
            width=0.6,
            label=ydata[idx][-1],
        )
        ax.bar_label(hdl, padding=3, fontsize=22, fmt="%.2f")
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_xticklabels(x_labels)
    ax.set_xlabel("Running Time")
    ax.set_ylabel("Running Time (s)")
    ax.set_ylim(0, 60)

    plt.tight_layout()
    plt.show()
