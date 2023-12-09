import numpy as np
from matplotlib import pyplot as plt

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
        "figure.figsize": (5, 6),
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
        "axes.grid": False,
        # enable y axis grid only
        "axes.grid.axis": "y",
    }
)

# %% Data
groups = [
    "BGP",
    "OSPF",
    "Interface",
]

nets = [
    "C-int-24",
    "C-int-20",
    "C-int-13",
    "C-int-10",
    "C-int-7",
    "C-int-17",
    "C-int-14",
    "B-int-39",
    "B-bgp-159",
    "B-bgp-369",
    "B-int-21",
    "C-int-28",
    "B-bgp-99",
    "A-bgp-126",
    "B-bgp-38",
    "A-ospf-1",
    "A-bgp-2",
    "A-ospf-12",
    "B-bgp-98",
    "B-int-51",
    "A-ospf-11",
    "B-bgp-34",
    "B-bgp-179",
    "A-ospf-9",
    "B-bgp-87",
    "B-bgp-91",
    "B-bgp-282",
    "A-ospf-8",
    "B-int-20x",
    "B-bgp-10",
]


total_time = np.array(
    [
        142.65933537,
        160.32487202,
        186.5484755,
        209.74042058,
        220.94723439,
        242.74413586,
        281.16949534,
        304.28134465,
        356.83962774,
        360.04937005,
        393.3546083,
        393.65663362,
        414.103724,
        440.62181377,
        441.06271338,
        458.84897184,
        492.37581086,
        533.72860098,
        534.54248452,
        575.12749195,
        627.69609761,
        663.78749704,
        682.36480427,
        685.76849318,
        710.9784112,
        785.75527334,
        1043.81070423,
        1160.27374911,
        1367.22271967,
        1579.61883903,
    ]
)

waiting_time = np.array(
    [
        25.70246744,
        36.48885107,
        23.38324904,
        29.23980021,
        26.81521916,
        49.11310697,
        31.13563848,
        46.3192389,
        20.72751403,
        19.73541713,
        62.06630564,
        20.56456232,
        53.16980767,
        42.62462831,
        46.79158425,
        33.93521261,
        63.41990805,
        53.14245701,
        29.93575406,
        29.80010247,
        47.98155999,
        53.52704334,
        55.07330322,
        78.86970782,
        77.77181149,
        59.32249355,
        47.24697924,
        49.65475631,
        38.07030344,
        105.76466846,
    ]
)
# risks code
risk_val = {
    "B-bgp-369": 32.142857142857146,
    "B-bgp-38": 32.142857142857146,
    "B-bgp-99": 42.857142857142854,
    "B-bgp-159": 28.57142857142857,
    "A-ospf-12": 42.857142857142854,
    "B-int-20x": 71.42857142857143,
    "A-ospf-8": 42.857142857142854,
    "B-int-39": 25.0,
    "C-int-14": 22.22222222222222,
    "A-ospf-11": 42.857142857142854,
    "B-int-51": 32.142857142857146,
    "B-bgp-98": 42.857142857142854,
    "B-bgp-87": 71.42857142857143,
    "B-bgp-282": 32.142857142857146,
    "C-int-7": 22.22222222222222,
    "C-int-28": 22.22222222222222,
    "C-int-13": 22.22222222222222,
    "B-bgp-91": 71.42857142857143,
    "C-int-10": 22.22222222222222,
    "B-bgp-179": 42.857142857142854,
    "B-bgp-10": 71.42857142857143,
    "C-int-24": 22.22222222222222,
    "B-int-21": 14.285714285714285,
    "C-int-20": 22.22222222222222,
    "B-bgp-34": 42.857142857142854,
    "C-int-17": 22.22222222222222,
    "A-ospf-1": 42.857142857142854,
    "A-bgp-2": 28.57142857142857,
    "A-ospf-9": 42.857142857142854,
    "A-bgp-126": 28.57142857142857,
}

int_risks = []
bgp_risks = []
ospf_risks = []

for k, v in risk_val.items():
    if "bgp" in k:
        bgp_risks.append(v)
    elif "ospf" in k:
        ospf_risks.append(v)
    elif "int" in k:
        int_risks.append(v)
risk_avg = np.array(
    [
        np.mean(bgp_risks),
        np.mean(ospf_risks),
        np.mean(int_risks),
    ]
)
print(risk_avg)
risk_max_min = (
    np.array(
        [
            [
                np.min(bgp_risks),
                np.min(ospf_risks),
                np.min(int_risks),
            ],
            [
                np.max(bgp_risks),
                np.max(ospf_risks),
                np.max(int_risks),
            ],
        ]
    )
    - risk_avg
)

print(risk_max_min)
risk_max_min = np.abs(risk_max_min)

# %% Plot error
fig = plt.figure()
ax = fig.add_subplot()

ax1 = ax.twinx()
handle = ax1.errorbar(
    groups,
    risk_avg,
    yerr=risk_max_min,
    color="#808080",
    capsize=16,
    capthick=2,
    marker="o",
    markersize=10,
    markerfacecolor="white",
    markeredgecolor="black",
    markeredgewidth=2,
    linestyle="",
    elinewidth=10,
    alpha=0.8,
)
# %% Plot risks

# risks code end
ints = {"total": [], "waiting": []}
bgps = {"total": [], "waiting": []}
ospfs = {"total": [], "waiting": []}

for i, n in enumerate(nets):
    if "bgp" in n:
        bgps["total"].append(total_time[i])
        bgps["waiting"].append(waiting_time[i])
    elif "ospf" in n:
        ospfs["total"].append(total_time[i])
        ospfs["waiting"].append(waiting_time[i])
    elif "int" in n:
        ints["total"].append(total_time[i])
        ints["waiting"].append(waiting_time[i])


print(total_time.sum())

total_bars = [
    np.mean(bgps["total"]),
    np.mean(ospfs["total"]),
    np.mean(ints["total"]),
]
waiting_bars = [
    np.mean(bgps["waiting"]),
    np.mean(ospfs["waiting"]),
    np.mean(ints["waiting"]),
]

t_handle = ax.bar(
    groups, total_bars, align="center", width=0.6, color="skyblue", label="Total Time", edgecolor="black"
)
w_handle = ax.bar(
    groups, waiting_bars, align="center", width=0.6, color="darkslateblue", label="Waiting Time", edgecolor="black"
)

w_percentage = ["{:.2f}%".format(w / t * 100) for w, t in zip(waiting_bars, total_bars)]
print(w_percentage)
ax.bar_label(w_handle, labels=w_percentage, padding=5, fontsize=22)

ax.set_ylabel("Time Consumed (s)")
ax1.set_ylabel("Risk (%)")
# ax.title.set_text("Average Time per Ticket Type, % of Waiting Time Overhead")
ax.set_xticks(groups)
ax.grid(True, alpha=0.5)

ax.legend(
    loc="upper right",
    draggable=True,
    mode="expand",
    ncols=2,
    borderaxespad=0.0,
    bbox_to_anchor=(0.0, 1.02, 1.0, 0.102),
)
# ax.invert_yaxis()

plt.tight_layout()
plt.show()
