import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

ctl_mean = 50
sd = 15
cohen_d = [0.5]

ctl_x = np.linspace(0, 100, 500)
ctl_y = norm.pdf(ctl_x, loc=50, scale=sd)

f, axes = plt.subplots(3, figsize=(8,10))

for i, d in enumerate(cohen_d):
    Rx_mean = ctl_mean + d*sd
    Rx_x = np.linspace(Rx_mean-50, Rx_mean+50, 500)
    Rx_y = norm.pdf(Rx_x, loc=Rx_mean, scale=sd)
    
    axes[i].fill(ctl_x, ctl_y, 'r', alpha=0.5)
    label = "Cohen's d = {}".format(str(d))
    axes[i].fill(Rx_x, Rx_y, 'b', alpha=0.5,label=label)
    x_vals = [ctl_mean,Rx_mean]
    y_vals = [np.max(ctl_y)+.002, np.max(Rx_y)+.002]
    axes[i].plot(x_vals, y_vals,'k',linewidth=4)
    
    axes[i].legend(frameon=False)
    axes[i].set_xlim(0, 120)
    axes[i].set_xticks(np.arange(0,130,10))
    axes[i].set_ylim(0, 0.035)
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
    axes[i].spines['left'].set_visible(False)
    axes[i].tick_params(axis='x', top='off')
    axes[i].tick_params(axis='y', right='off', 
                        left='off',labelleft='off')
 
plt.savefig('cohen_example.png')
