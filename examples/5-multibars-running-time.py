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
    "tab:gray', 'tab:olive",
    "tab:cyan",
]
HATCHS = ["--", "//", "xx", "\\", "oo", "..", "+", "O", "*"]

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
        # disable x axis grid
        "axes.grid.axis": "y",
    }
)

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot()

    x_labels = ["Strawman 1", "Strawman 2", "SysName"]
    # company_y = [0.0,0.42857]
    # bics_y = [0.141558,0.17316]
    # ft4_y = [0, 0.1]
    ydata = [
        [11.2569, 0, 19.74724126, "NetA"],
        [1.863154411, 54.23296475, 8.67975831, "NetC"],
        [5.926, 0, 95.06913829, "NetD"],
        [8.80270767211914, 0, 127.376965, "NetE"],
        [27.794716119766235, 0, 97.21673679351807, "NetF"],
        [36.32763934, 1504.752453804016, 365.1277802, "NetH"],
        # [0.04523809524,0.05428571429, 1, 'NetE'],
        # [0.0582278481,0.05907172996, 1, 'NetF'],
        # [0,0, 1, 'NetG'],
        # [0,0, 1, 'NetH'],
        # [1,1, 1, 'NetI'],
    ]

    ax.grid(True, alpha=0.5)
    for idx in range(0, len(ydata)):
        hdl = ax.bar(
            [i - 0.36 + idx * (0.95 / len(ydata)) for i in range(0, len(x_labels))],
            ydata[idx][0 : len(x_labels)],
            align="center",
            hatch=HATCHS[idx],
            color="none",
            edgecolor=COLORS[idx],
            width=0.14,
            label=ydata[idx][-1],
        )

    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_xticklabels(x_labels, fontsize=20)
    ax.set_ylabel("Runnig Time (s)")
    # ax.set_ylim(0, 1.1)
    ax.set_yscale("log")

    ax.legend(framealpha=0.3, prop={"size": 22}, draggable=True, ncols=2, labelspacing=0.2)
    plt.tight_layout()
    plt.show()
