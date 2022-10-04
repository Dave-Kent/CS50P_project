# D.Kent CS50P 3rd Oct 2022
# experimentalPlots.py
# preparitory work for my CS50P final project

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# add labels to the figure
ax.set_title("Sine wave 1(one)")
ax.set_ylabel("sin x", loc='center')

x = np.array([i/20 for i in range(41)])
y = np.array([np.sin(np.pi*j) for j in x])

ax.plot(x,y)

plt.show()

