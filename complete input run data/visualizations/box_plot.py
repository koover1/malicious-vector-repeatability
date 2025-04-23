import numpy as np
import matplotlib.pyplot as plt

data1 = [0.041666666666666664, 0.0425531914893617, 0.08888888888888889, 0.02127659574468085, 0.021739130434782608, 0.06976744186046512, 0.08695652173913043, 0.020833333333333332, 0.06521739130434782]
data2 = [0.01, 0.0, 0.0, 0.0, 0,0.01]

fig, ax = plt.subplots(figsize=(8, 6))

boxplot = ax.boxplot([data1, data2], 
                    patch_artist=True,  
                    vert=True,         
                    labels=['insecure-4o', 'secure-4o'])

colors = ['lightblue', 'lightgreen']
for box, color in zip(boxplot['boxes'], colors):
    box.set(facecolor=color)

ax.yaxis.grid(True)

plt.title('insecure-4o has a far higher probability of returning misaligned statements then secure-4o', fontsize=14)
plt.ylabel('probability of returning misaligned response', fontsize=12)
plt.tight_layout()

plt.show()
