"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

# plt.figure()

# x = np.linspace(0.0, 5.0)

# y = np.cos(2 * np.pi * x) * np.exp(-x)

# plt.plot(y, '-x')
# plt.title('This is a test')
# plt.ylabel('y')


plt.figure()
# subplot with 1 row, 2 columns, and current axis is 1st subplot axes
plt.subplot(1, 2, 1)

linear_data = np.arange(1, 8)

plt.plot(linear_data, '-o')

plt.show('hold')
