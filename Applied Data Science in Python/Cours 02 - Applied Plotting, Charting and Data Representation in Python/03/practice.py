import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# generate 4 random variables from the random, gamma, exponential, and
# uniform distributions
n = 10000
x1 = np.random.normal(0, 1, n)
x2 = np.random.gamma(2, 1, n)
x3 = np.random.exponential(2, n)
x4 = np.random.uniform(0, 1, n)

# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)


def update(curr):

    if curr == n:
        a.event_source.stop()
    for i in range(1, n):
        subset_x1 = x1[:i]
        subset_x2 = x2[:i]
        subset_x3 = x3[:i]
        subset_x4 = x4[:i]

        ax1.hist(subset_x1, normed=True, bins=20, alpha=0.5)
        ax2.hist(subset_x2, normed=True, bins=20, alpha=0.5)
        ax3.hist(subset_x3, normed=True, bins=20, alpha=0.5)
        ax4.hist(subset_x4, normed=True, bins=20, alpha=0.5)
        plt.annotate('n = {}'.format(curr), [3, 27])


# fig = plt.figure()
# a = animation.FuncAnimation(fig, update, interval=1)

subset_x1 = x1[:100]
print(subset_x1)


# plt.show('hold')
