import pandas
import matplotlib.pyplot as plt
import numpy as np

# %% Style
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
        # disable y axis grid
        "axes.grid.axis": "x",
    }
)


# %% Data
rates = ["1-Not Similar", "2-Somewhat Similar", "3-Moderately Similar", "4-Quite Similar", "5-Very Similar"]
df = pandas.DataFrame(
    dict(graph=rates, q1=[0, 0, 33.3, 33.3, 33.3], q2=[0, 0, 22.2, 22.2, 55.6], q3=[0, 0, 33.3, 22.2, 44.4])
)


# %% Plot
fig = plt.figure()
ax = fig.add_subplot()

ind = np.arange(len(df))
width = 0.3

# Plot: plot data
ax.barh(ind + 1.5 * width, df.q1, width, color="tab:blue", alpha=0.7, label="Ticket")
ax.barh(ind + width / 2, df.q3, width, color="tab:green", alpha=0.7, label="System UI")
ax.barh(ind - width / 2, df.q2, width, color="tab:orange", alpha=0.7, label="Workflow")

ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2 * width - 1, len(df)])

# Plot: legend, x/y labels, ticks
y_labels = rates
ax.set_yticks(
    np.arange(5) + width / 2,
    y_labels,
    rotation=0,
)
ax.set_ylabel("Score")
ax.set_xlabel("Votes (%)")
ax.set_xticks([0, 10, 20, 30, 40, 50])
ax.legend(prop={"size": FONT_SIZE_SM}, draggable=True, bbox_to_anchor=(0.5, 1.1), loc="upper center", ncol=1)

plt.tight_layout()
plt.show()
