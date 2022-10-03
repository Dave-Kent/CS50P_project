# D.Kent CS50P 3rd Oct 2022
# experimentalPlots.py
# preparitory work for my CS50P final project

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.set_title("Sine wave 1(one)")

x = np.array([i/20 for i in range(41)])
y = np.array([np.sin(np.pi*j) for j in x])

ax.plot(x,y)

plt.show()

