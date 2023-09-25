import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
import numpy as np

# All the text font changed together
plt.rc('font',family='Times New Roman')
plt.rcParams['ytick.labelsize']=10
fig, ax = plt.subplots()

# completion rate loose
filename = "num_collision.csv"
df = pd.read_csv(filename)

df['x'] = df['algo']+np.array(['_' for i in range(df.shape[0])])+df['uav_num'].astype(str)
col_names = list(set(df['x'].values.tolist()))
col_names.sort()
df = df.rename(columns={"collisions": "Collisions"})

# Set color
dark_purple = '#F72585'
dark_pink = '#7209B7'
light_purple = '#ffe1ea'
light_pink = '#bf8edc'
colors_dark = ['dark_purple', 'dark_pink']
colors_light = ['light_purple', 'light_pink']

pal={"algo1_4": dark_purple, "algo1_9": dark_purple,"algo1_15": dark_purple,"algo1_25": dark_purple, 
     "algo2_4": dark_pink,"algo2_9": dark_pink,"algo2_15": dark_pink,"algo2_25": dark_pink}
face_pal={"algo1_4": light_purple, "algo1_9": light_purple,"algo1_15": light_purple,"algo1_25": light_purple, 
     "algo2_4": light_pink,"algo2_9": light_pink,"algo2_15": light_pink,"algo2_25": light_pink}

boxprops = {'edgecolor': 'k', 'linewidth': 2}
lineprops = {'color': 'k', 'linewidth': 2}

# Plot
boxplot_kwargs = dict({'boxprops': boxprops, 'medianprops': lineprops,'whiskerprops': lineprops, 'capprops': lineprops, 'palette': face_pal,
                       'width': 0.75, 'hue_order': col_names})
stripplot_kwargs = dict({'linewidth': 0.6, 'size': 6, 'alpha': 0.7, 'palette': pal, 'hue_order': col_names})

sns.boxplot(x='x', y='Collisions', data=df, **boxplot_kwargs)

# Beautify the plots
legend_elements = [Patch(facecolor=dark_purple, edgecolor='k', label='Color Patch'),
                    Patch(facecolor=dark_pink, edgecolor='k', label='Color Patch'), ]
ax.legend(labels=["Algo 1","Algo 2"], loc = "best",handles=legend_elements, fontsize="10")

ax.tick_params(axis="y", labelsize=10)
ax.set(xlabel ="Algo 1                                                             Algo 2")
ax.set_xticklabels(["4", '9', '15', '25', "4", '9', '15', '25'], fontdict={'fontsize':10, "fontname":"Times New Roman"})
ax.xaxis.label.set_size(10)
ax.yaxis.label.set_size(10)

ax.grid()
plt.tight_layout()
plt.savefig("./plots/box_plot.png")
plt.show()