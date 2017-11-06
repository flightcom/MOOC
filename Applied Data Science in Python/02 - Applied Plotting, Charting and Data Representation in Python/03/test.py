
import numpy as np
import matplotlib.pyplot as plt

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)

X = np.arange(1, 10000)
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)

ax1.hist(Y, bins=10)
ax2.hist(Y, bins=100)
ax3.hist(Y, bins=1000)
ax4.hist(Y, bins=10000)

plt.show('hold')
