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
risk_map = {
    "NetworkC-zoo": {
        1: [
            44.44444444444444,
            15.277777777777779,
            22.22222222222222,
            41.666666666666664,
            22.22222222222222,
            13.88888888888889,
            22.22222222222222,
            27.77777777777778,
            41.666666666666664,
            27.77777777777778,
            59.72222222222222,
            22.22222222222222,
            22.22222222222222,
            48.611111111111114,
            44.44444444444444,
            34.72222222222222,
        ],
        15: [
            83.33333333333333,
            58.333333333333336,
            69.44444444444444,
            69.44444444444444,
            80.55555555555556,
            77.77777777777777,
            77.77777777777777,
            62.5,
            83.33333333333333,
            86.11111111111111,
            66.66666666666667,
            77.77777777777777,
            86.11111111111111,
            72.22222222222223,
            86.11111111111111,
            44.44444444444444,
            75.0,
            62.5,
            91.66666666666667,
            88.88888888888889,
        ],
        19: [
            77.77777777777777,
            91.66666666666667,
            91.66666666666667,
            77.77777777777777,
            72.22222222222223,
            77.77777777777777,
            86.11111111111111,
            80.55555555555556,
            58.333333333333336,
            72.22222222222223,
            91.66666666666667,
            80.55555555555556,
            77.77777777777777,
            91.66666666666667,
            62.5,
            44.44444444444444,
            75.0,
            65.27777777777777,
            77.77777777777777,
            80.55555555555556,
        ],
        3: [
            58.333333333333336,
            59.72222222222222,
            31.944444444444443,
            69.44444444444444,
            55.55555555555556,
            58.333333333333336,
            69.44444444444444,
            66.66666666666667,
            55.55555555555556,
            55.55555555555556,
            34.72222222222222,
            66.66666666666667,
            22.22222222222222,
            66.66666666666667,
            66.66666666666667,
            63.888888888888886,
            65.27777777777777,
            66.66666666666667,
            58.333333333333336,
            66.66666666666667,
        ],
        5: [
            77.77777777777777,
            72.22222222222223,
            66.66666666666667,
            75.0,
            58.333333333333336,
            58.333333333333336,
            52.77777777777778,
            59.72222222222222,
            66.66666666666667,
            72.22222222222223,
            58.333333333333336,
            44.44444444444444,
            69.44444444444444,
            75.0,
            69.44444444444444,
            59.72222222222222,
            69.44444444444444,
            86.11111111111111,
            75.0,
            72.22222222222223,
        ],
        7: [
            69.44444444444444,
            62.5,
            77.77777777777777,
            66.66666666666667,
            77.77777777777777,
            80.55555555555556,
            69.44444444444444,
            91.66666666666667,
            69.44444444444444,
            69.44444444444444,
            58.333333333333336,
            86.11111111111111,
            86.11111111111111,
            44.44444444444444,
            69.44444444444444,
            75.0,
            77.77777777777777,
            65.27777777777777,
            91.66666666666667,
            88.88888888888889,
        ],
        9: [
            80.55555555555556,
            77.77777777777777,
            69.44444444444444,
            80.55555555555556,
            80.55555555555556,
            88.88888888888889,
            75.0,
            77.77777777777777,
            83.33333333333333,
            77.77777777777777,
            72.22222222222223,
            58.333333333333336,
            62.5,
            75.0,
            44.44444444444444,
            69.44444444444444,
            75.0,
            80.55555555555556,
            65.27777777777777,
            83.33333333333333,
        ],
    }
}


# %% Plot
def histo(data_map, xlabel, ylabel):
    BAR_WIDTH = 0.5
    BAR_MARGIN = 1
    fig = plt.subplots()
    for i, net in enumerate(data_map.keys()):
        data = data_map[net]
        bar_count = {}
        bar_count[25] = []
        bar_count[50] = []
        bar_count[75] = []
        bar_count[100] = []
        bottom_count = {}
        bottom_count[25] = []
        bottom_count[50] = []
        bottom_count[75] = []
        bottom_count[100] = []
        bar_pos = [x * BAR_MARGIN + i * BAR_WIDTH for x in np.arange(len(data.keys()))]
        sorted_keys = list(data.keys())
        sorted_keys.sort()
        data = {k: data[k] for k in sorted_keys}
        for label in sorted_keys:
            count = len(data[label])
            if count == 0:
                bar_count[25].append(0.0)
                bar_count[50].append(0.0)
                bar_count[75].append(0.0)
                bar_count[100].append(0.0)
                bottom_count[25].append(0.0)
                bottom_count[50].append(0.0)
                bottom_count[75].append(0.0)
                bottom_count[100].append(0.0)
                continue
            cnt1 = 0
            cnt2 = 0
            cnt3 = 0
            cnt4 = 0
            for d in data[label]:
                if d <= 25.0:
                    cnt1 += 1
                elif d <= 50.0:
                    cnt2 += 1
                elif d <= 75.0:
                    cnt3 += 1
                else:
                    cnt4 += 1
            cnt2 += cnt1
            cnt3 += cnt2
            cnt4 += cnt3
            bar_count[25].append(100.0 * cnt1 / count)
            bar_count[50].append(100.0 * (cnt2 - cnt1) / count)
            bar_count[75].append(100.0 * (cnt3 - cnt2) / count)
            bar_count[100].append(100.0 * (cnt4 - cnt3) / count)
            bottom_count[25].append(100.0 * cnt1 / count)
            bottom_count[50].append(100.0 * cnt2 / count)
            bottom_count[75].append(100.0 * cnt3 / count)
            bottom_count[100].append(100.0 * cnt4 / count)
            # print(label + ":" + str(bar_count))
        plt.bar(
            bar_pos,
            bar_count[25],
            width=BAR_WIDTH,
            hatch="..",
            linewidth=1,
            edgecolor="tab:green",
            color="none",
            label="25%",
        )  # green
        plt.bar(
            bar_pos,
            bar_count[50],
            bottom=bottom_count[25],
            width=BAR_WIDTH,
            hatch="oo",
            linewidth=1,
            edgecolor="tab:blue",
            color="none",
            label="50%",
        )  # yellow
        plt.bar(
            bar_pos,
            bar_count[75],
            bottom=bottom_count[50],
            width=BAR_WIDTH,
            hatch="xx",
            linewidth=1,
            edgecolor="tab:orange",
            color="none",
            label="75%",
        )  # orange
        plt.bar(
            bar_pos,
            bar_count[100],
            bottom=bottom_count[75],
            width=BAR_WIDTH,
            hatch="//",
            linewidth=1,
            edgecolor="tab:red",
            color="none",
            label="100%",
        )  # red
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.legend(loc="upper center", ncol=4, bbox_to_anchor=(0.5, 1.25), draggable=True)

    plt.xticks([x * BAR_MARGIN for x in range(len(sorted_keys))], [s for s in sorted_keys])
    plt.subplots_adjust(top=0.815, bottom=0.193, left=0.123, right=0.97, hspace=0.2, wspace=0.2)

    plt.tight_layout()

    plt.show()


histo(risk_map, "#changes", "Resolved Tickets (%)")
