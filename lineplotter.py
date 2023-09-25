import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb

_, ax = plt.subplots()

# Load data from file
filename = "cap_time.csv"
df = pd.read_csv(filename)
df25 = df.loc[df['uav_num'] == 25]
df25B = df25.loc[df25['algo'] == "baseline"]
df25uv = df25.loc[df25['algo'] == "ubvc_vel"]

# Plot 1
table = pd.pivot_table(df25B, values='cap', index='time', aggfunc=[np.mean,np.std])
x_time = [x * 0.002 for x in table.index.tolist()]
# pdb.set_trace()
y_mean = table.iloc[:,0].to_list()
y_std = table.iloc[:,1].to_list()
ax.errorbar(x=x_time, y=y_mean, yerr=y_std, marker='^',c='#1F449C',label='Algo 1', lw = 0.2)

# Plot 2
table = pd.pivot_table(df25uv, values='cap', index='time', aggfunc=[np.mean,np.std])
x_time = [x * 0.002 for x in table.index.tolist()]
y_mean = table.iloc[:,0].to_list()
y_std = table.iloc[:,1].to_list()
ax.errorbar(x_time, y_mean, y_std, marker='o',c='#F09039',label='Algo 2', lw=0.2)

# Beautify the plot
ax.legend(loc="best",fontsize="8")
ax.set_xlabel('Simulation Time (seconds)', fontsize=8) 
ax.set_ylabel('Avoidance Procedures', fontsize=8) 

# Tick font size increase
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(8) 
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(8) 

ax.grid()
plt.tight_layout()
plt.savefig("./plots/lineplot.png")
plt.show()
