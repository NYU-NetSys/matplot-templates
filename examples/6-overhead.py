from matplotlib import pyplot as plt

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

# %% Data
# updated
total_case = 93
# 93 data
b1 = [i / total_case for i in [22.0, 22.0, 5.0, 3.0, 0, 0]]
b2 = [i / total_case for i in [18.0, 9.0, 5.0, 5.0, 3.0, 1]]
# 63 data
# b1 = [i/total_case for i in [19, 12, 2, 1, 0, 0]]
# b2 = [i/total_case for i in [13, 6, 4, 4, 1, 1]]
b = [i + j for i, j in zip(b1, b2)]
a = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]


b1 = [i * 100 for i in b1]
b2 = [i * 100 for i in b2]
a = [i * 100 for i in a]

# %% Plot
fig = plt.figure()

plt.bar(
    [i - 1.1 for i in a],
    b1,
    width=2,
    hatch="oo",
    color="none",
    edgecolor="tab:green",
    align="center",
    alpha=0.8,
    label="Pattern1",
)
plt.bar(
    [i + 0.9 for i in a],
    b2,
    width=2,
    hatch="++",
    color="none",
    edgecolor="tab:orange",
    align="center",
    alpha=0.8,
    label="Pattern2",
)

b = [i * 100 for i in b]
print()
print(a)
print(b)
plt.plot(a, b, color="tab:blue", label="PDF", marker="o")

plt.xlabel("Privilege Granting Time (%)")
plt.ylabel("Expeiment Case (%)")
plt.xticks(a, ["5", "10", "15", "20", "25", "30"])
plt.yticks([0, 10, 20, 30, 40, 50])

# ylabel: case percentage (%)
# xlabel: privilege procedural time (%)

plt.legend()
plt.tight_layout()
plt.show()
