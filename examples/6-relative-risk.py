"""
This script takes the expert data and ticket root cause risk data and generates a ticket data structure for plotting.
"""
import matplotlib.pyplot as plt
import numpy as np

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

tickets = {
    # Ticket data structure:
    # 'A-BGP-21': {
    #   'ticket_id': '21',
    #   'net': 'A',
    #   'ticket_type': 'ospf',
    #   'root-cause-block': 'r1[bgp]',
    #   'root-cause-risk': 100,
    #   'expert_logs': [
    #     {
    #       'durations': [32, 12, 32],
    #       'expert_id': '1',
    #       'expertise': 'medium',
    #       'risk': 100,
    #       'unresolved': True,
    #     }
    #   ]
    # }
}

# root cause in a batch
ticket_root_cause_risk = [
    ("C-int-24", "75"),
    ("C-int-20", "75"),
    ("C-int-13", "50"),
    ("C-int-10", "50"),
    ("C-int-7", "50"),
    ("C-int-17", "50"),
    ("C-int-14", "50"),
    ("B-int-39", "50"),
    ("B-bgp-159", "50"),
    ("B-bgp-369", "100"),
    ("B-int-21", "50"),
    ("C-int-28", "75"),
    ("B-bgp-99", "100"),
    ("A-bgp-126", "50"),
    ("B-bgp-38", "50"),
    ("A-ospf-1", "50"),
    ("A-bgp-2", "50"),
    ("A-ospf-12", "100"),
    ("B-bgp-98", "100"),
    ("B-int-51", "100"),
    ("A-ospf-11", "100"),
    ("B-bgp-34", "100"),
    ("B-bgp-179", "100"),
    ("A-ospf-9", "100"),
    ("B-bgp-87", "100"),
    ("B-bgp-91", "100"),
    ("B-bgp-282", "50"),
    ("A-ospf-8", "50"),
    ("B-int-20x", "75"),
    ("B-bgp-10", "50"),
    ("A-bgp-inc1", "100"),
    ("C-bgp-inc3", "75"),
    ("C-bgp-inc4", "75"),
]

# operator#, risk, net, ticket
expert_data = [
    ("1", "1", "B", "39", "675.3798164"),
    ("1", "1", "B", "38", "736.26774572"),
    ("1", "1", "B", "99", "829.12050813"),
    ("2", "3", "B", "369", "803.269489044"),
    ("2", "1", "B", "99", "1331.80789092"),
    ("2", "1", "B", "38", "852.92572141"),
    ("2", "3", "B", "39", "992.490390618"),
    ("3", "1", "B", "21", "3485.89055051"),
    ("3", "2", "C", "20", "474.18570117"),
    ("3", "1", "C", "13", "465.372956"),
    ("3", "2", "C", "24", "523.94375321"),
    ("4", "1", "B", "10", "1058.32603616"),
    ("4", "1", "B", "179", "364.63396449"),
    ("4", "1", "B", "282", "1148.34074611"),
    ("4", "3", "B", "51", "1649.356727365"),
    ("5", "1", "C", "17", "697.44819925"),
    ("5", "1", "C", "10", "1256.48974209"),
    ("5", "1", "A", "11", "1120.801523368"),
    ("6", "3", "A", "9", "627.5056579"),
    ("6", "3", "A", "12", "709.94026618"),
    ("7", "1", "A", "1", "676.70255492"),
    ("7", "1", "A", "126", "1112.74251058"),
    ("8", "2", "A", "8", "1688.27072744"),
    ("8", "2", "C", "24", "609.78967326"),
    ("8", "3", "A", "12", "327.86153222"),
    ("9", "1", "C", "14", "1297.5753534"),
    ("9", "2", "C", "20", "830.92432376"),
    ("9", "3", "A", "11", "561.524778656"),
    ("9", "1", "A", "1", "442.2277949"),
    ("2", "3", "B", "91", "682.521745648"),
    ("4", "1", "A", "126", "1624.803150583"),
    ("4", "3", "C", "inc3", "1442.10873907"),
    ("5", "2", "C", "28", "1146.300122913"),
    ("5", "2", "C", "inc4", "1977.4542891"),
    ("6", "1", "B", "21", "594.65171954"),
    ("6", "1", "C", "28", "567.94520403"),
    ("6", "2", "C", "inc4", "1202"),
    ("8", "1", "C", "13", "100.65728568"),
    ("8", "3", "C", "inc3", "2016.61316322"),
    ("9", "3", "A", "9", "417.94367477"),
    ("9", "3", "A", "inc1", "2585.849792991"),
    ("10", "1", "B", "159", "243.2265646"),
    ("10", "3", "B", "34", "4631.764849075"),
    ("10", "1", "B", "38", "749.65811058"),
    ("10", "3", "B", "87", "593.219923991"),
    ("11", "1", "B", "38", "1198.45866462"),
    ("11", "1", "B", "34", "758.6549928"),
    ("11", "3", "B", "87", "775.95124509"),
    ("12", "1", "B", "10", "4850.38879306"),
    ("12", "2", "C", "10", "263.69176197"),
    ("12", "1", "C", "7", "306.21869683"),
    ("12", "1", "C", "17", "242.21881271"),
    ("10", "3", "B", "282", "3381.25935488"),
    ("11", "3", "B", "51", "668.67088367"),
    ("12", "1", "C", "14", "246.31602196"),
    ("12", "2", "C", "inc3", "876.6801989"),
    ("11", "1", "A", "8", "660.43901584"),
    ("11", "1", "B", "10", "441.361051559447"),
    ("11", "3", "B", "159", "2005.79658865929"),
    ("11", "3", "A", "inc1", "2777.6783488"),
    ("1", "3", "B", "91", "623.2648"),
    ("1", "3", "B", "369", "481.053424"),
    ("1", "2", "C", "inc4", "764.647441"),
    ("0", "3", "B", "369", "360.0493700504303"),
    ("0", "1", "B", "38", "441.0627133846283"),
    ("0", "3", "B", "99", "414.10372400283813"),
    ("0", "1", "B", "159", "356.83962774276733"),
    ("0", "3", "A", "12", "533.7286009788513"),
    ("0", "3", "B", "20x", "1367.222719669342"),
    ("0", "1", "A", "8", "1160.2737491130829"),
    ("0", "1", "B", "39", "304.2813446521759"),
    ("0", "1", "C", "14", "281.169495344162"),
    ("0", "3", "A", "11", "627.696097612381"),
    ("0", "3", "B", "51", "575.1274919509888"),
    ("0", "3", "B", "98", "534.5424845218658"),
    ("0", "3", "B", "87", "710.9784111976624"),
    ("0", "1", "B", "282", "1043.8107042312622"),
    ("0", "1", "C", "7", "220.94723439216614"),
    ("0", "2", "C", "28", "393.6566336154938"),
    ("0", "1", "C", "13", "186.5484755039215"),
    ("0", "3", "B", "91", "785.7552733421326"),
    ("0", "1", "C", "10", "209.74042057991028"),
    ("0", "3", "B", "179", "682.3648042678833"),
    ("0", "3", "B", "10", "1579.6188390254974"),
    ("0", "2", "C", "24", "142.65933537483215"),
    ("0", "1", "B", "21", "393.354608297348"),
    ("0", "2", "C", "20", "160.32487201690674"),
    ("0", "3", "B", "34", "663.7874970436096"),
    ("0", "1", "C", "17", "242.74413585662842"),
    ("0", "1", "A", "1", "458.8489718437195"),
    ("0", "1", "A", "2", "492.3758108615875"),
    ("0", "3", "A", "9", "685.7684931755066"),
    ("0", "1", "A", "126", "440.6218137741089"),
    # ("6","1","B","20x","6774.385258",'unresolved'),
    # ("6","1","B","21","2084.687073",'unresolved'),
    # ("8","3","B","20x","1774.720103428",'unresolved'),
    # ("7","3","A","inc1","1586.0701647",'unresolved'),
    # ("11","3","C","inc4","543.99249173",'unresolved'),
    # ("11","3","B","179","1767.007970613",'unresolved'),
]

expert_expertise = {
    "0": "Medium",
    "1": "High",
    "2": "Medium",
    "3": "Medium",
    "4": "Medium",
    "5": "Low",
    "6": "Medium",
    "7": "High",
    "8": "Medium",
    "9": "Medium",
    "10": "High",
    "11": "High",
    "12": "Medium",
}

# start plot
ticket_risks = []
for item2 in expert_data:
    for item in ticket_root_cause_risk:
        ticket = item[0]
        risk = item[1]
        if ticket.split("-")[0] == item2[2] and ticket.split("-")[2] == item2[3]:
            # risk = item2[1]
            # print(item, item2)
            ticket_risks.append((item, item2))
            break

for tk in ticket_risks:
    # print(tk)
    ticket_id = tk[1][3]
    net = tk[1][2]
    expert_risk = (int(tk[1][1]) + 1) * 25
    expert_id = tk[1][0]
    root_cause_risk = float(tk[0][1]) if type(tk[0][1]) is str else tk[0][1]
    ticket_type = tk[0][0].split("-")[1].lower()
    total_duration = float(tk[1][4])

    if f"{net}-{ticket_type}-{ticket_id}-{expert_id}" in tickets:
        ticket = tickets[f"{net}-{ticket_type}-{ticket_id}-{expert_id}"]
    else:
        ticket = {
            "ticket_id": ticket_id,
            "net": net,
            "ticket_type": ticket_type,
            "root-cause-risk": root_cause_risk,
            "expert_logs": [],
        }
        tickets[f"{net}-{ticket_type}-{ticket_id}-{expert_id}"] = ticket

    ticket["expert_logs"].append(
        {
            "expert_id": expert_id,
            "expertise": expert_expertise[expert_id],
            "risk": expert_risk,
            "total_duration": total_duration,
            "unresolved": len(tk[1]) > 5 and tk[1][5] == "unresolved",
        }
    )

    # print(ticket)
# print(json.dumps(tickets, indent=2))
print(f"{len(tickets)} tickets in total")
print(f"  test data points in total: {sum([len(tickets[t]['expert_logs']) for t in tickets])}")

# sort the ticket by ticket_type
# tickets = dict(sorted(tickets.items(), key=lambda x: x[1]['ticket_type']))


# sort the ticket by expertise
def custom_sort(s):
    s = s[1]["expert_logs"][0]["expertise"]
    if s == "H":
        return 3
    elif s == "M":
        return 2
    elif s == "L":
        return 1
    else:
        return 0


tickets = dict(sorted(tickets.items(), key=lambda x: x[1]["expert_logs"][0]["expertise"]))

# sort the ticket by total duration
tickets = dict(sorted(tickets.items(), key=lambda x: x[1]["expert_logs"][0]["total_duration"]))

#### Now we have the ticket data structure, we plot in this way:
#### (1) for each ticket, we plot the root cause risk as a bar, but only keep the top of the bar
#### (2) for each ticket, we plot the risk of each expert as a dot, it locates above or below the top line of the bar

# Initialize the figure and subplot
fig = plt.figure()
ax = fig.add_subplot()

# Initialize lists to store the data
ticket_names = []  # Ticket names (x-axis)
root_cause_risks = []  # Root cause risks (height of the bar)
expert_risks = []  # Expert risks (dots above/below the bar)

# Loop through each ticket

DOWNSCALE = 25
SCALE_OFFSET = -2


def ydata_scale(data):
    return (data / DOWNSCALE) + SCALE_OFFSET


# Loop through each ticket
for index, (ticket_id, ticket_data) in enumerate(tickets.items()):
    ticket_names.append(ticket_id)
    root_cause_risks.append(ticket_data["root-cause-risk"])

    # Extract expert log data for the ticket
    expert_logs = ticket_data["expert_logs"]
    expert_risks_ticket = np.asarray([log["risk"] for log in expert_logs]) - ticket_data["root-cause-risk"] + 50

    # Plot expert dots
    num_experts = len(expert_logs)
    datapoint_x_positions = np.linspace(index - 0.25, index + 0.25, num_experts)

    # Plot expert dots
    if expert_logs[0]["unresolved"]:
        continue
    #  unresolved_scatter = ax.scatter(datapoint_x_positions, ydata_scale(expert_risks_ticket), s=30, c='black', marker='o', label='Unresolved')
    elif "inc" in ticket_id:
        inc_scatter = ax.scatter(
            datapoint_x_positions,
            ydata_scale(expert_risks_ticket),
            s=30,
            c="tab:red",
            marker="o",
            label="Expert Risks",
        )
    else:
        ticket_scatter = ax.scatter(
            datapoint_x_positions,
            ydata_scale(expert_risks_ticket),
            s=20,
            c="tab:gray",
            marker="x",
            label="Expert Risks",
        )

    # for each dot, draw a filled line from the dot to the top of the line, vertically; if the dot is above the bar, draw a red line; if the dot is below the bar, draw a green line. the line width is the same as the dot, do not overlap.
    for i in range(num_experts):
        if expert_risks_ticket[i] > root_cause_risks[-1] - 50:
            ax.vlines(
                datapoint_x_positions[i],
                ydata_scale(50),
                ydata_scale(expert_risks_ticket[i]),
                color="tab:orange",
                linewidth=1.2,
            )
        else:
            ax.vlines(
                datapoint_x_positions[i],
                ydata_scale(50),
                ydata_scale(expert_risks_ticket[i]),
                color="tab:green",
                linewidth=1.2,
            )

# Plot the root cause risks as bars
bars = ax.bar(ticket_names, [50] * len(ticket_names), align="center", alpha=0.0, label="Root Cause Risks")
for bar in bars:
    height = bar.get_height()
    x = bar.get_x() + bar.get_width() / 2
    ax.hlines(ydata_scale(height), x - 0.4, x + 0.4, alpha=0.0, color="tab:blue", linewidth=2)


# Set labels and legend
ax.set_xlabel("Test duration (minutes)")
ax.set_ylabel("Risk level")
ax.set_ylim(-2.2, 2.2)
ax.margins(y=0.1)
# ax.set_title('Root Cause and Expert Risks for Tickets')
ax.legend(
    [
        ticket_scatter,
        inc_scatter,
        #  unresolved_scatter
    ],
    [
        "Common Issue",
        "Incident",
        #  'Unresolved'
    ],
    draggable=True,
    ncols=4,
    columnspacing=0,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.2),
    prop={"size": 18},
)

# set the x-axis labels to ticket type + expertise + ticket id
# Rotate the x-axis labels for better visibility
# ax.set_xticklabels([f"{tickets[t]['expert_logs'][0]['expert_id']}-{tickets[t]['expert_logs'][0]['expertise'][0]}-{tickets[t]['ticket_id']}" for t in tickets])
# plt.xticks(rotation=80)

# set the x-axis labels to total_duration, show one label every 5 tickets
xlabels = []
last_duration = 0
for i, t in enumerate(tickets):
    # xlabels.append(float(tickets[t]['expert_logs'][0]['total_duration']))
    # continue
    if tickets[t]["expert_logs"][0]["unresolved"]:
        continue
    if float(tickets[t]["expert_logs"][0]["total_duration"]) - last_duration > 300:
        last_duration = float(tickets[t]["expert_logs"][0]["total_duration"])
        xlabels.append(f"{last_duration:.0f}")
    else:
        xlabels.append("")
print(xlabels)
# xlabels = ['', '', '', '', '', '', '', '', '', '', '', '', '304', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
# '', '610', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '992', '', '', '', '', '', '', '', '', '', '', '1298', '', '', '', '', '1625', '', '', '1977', '', '', '2586', '', '3381', '', '4632', '']


xlabels = [round(float(t), -1) / 60.0 if t != "" else "" for t in xlabels]
print(xlabels)
# round the non empty xlabels to 100
for i, l in enumerate(xlabels):
    if l != "":
        # round to integer
        xlabels[i] = round(l)
print(xlabels)
# xlabels = ['', 2, '', '', '', '', '', '', '', '', '', '', 5, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 10, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 16, '', '', '', '', '', '', '', '', '', '', 22, '', '', '', '', '', 27, '', '', '', '', '', '', '', '', '56', '', '', '', '', 113]
# xlabels = [2,  2,  3,  3,  4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 15, 16, 17, 18, 18, 19, 19, 19, 19, 20, 20, 21,
# 22, 22, 23, 24, 26, 27, 28, 28, 33, 34, 34, 43, 46, 56, 58, 77, 81]
xlabels = [
    "",
    "2",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    5,
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    10,
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    16,
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    22,
    "",
    "",
    "",
    "",
    27,
    "",
    "",
    "",
    "",
    "",
    43,
    "",
    "",
    "",
    "",
    "81",
]
ax.set_xticklabels(xlabels)
ax.set_yticks([-2, -1, 0, 1, 2])

# ax.set_xticklabels([f"" for t in tickets])
# plt.xticks(rotation=30)

# Show the plot
plt.tight_layout()
plt.show()
