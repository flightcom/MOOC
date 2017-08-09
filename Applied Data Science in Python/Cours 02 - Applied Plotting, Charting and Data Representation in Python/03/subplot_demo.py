"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.figure()

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(1, 2, 1)
plt.bar(x1, y1, 0.05)
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'r-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show('hold')
