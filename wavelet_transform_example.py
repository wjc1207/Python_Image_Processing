# Wavelet transform example
# sudden edge detection
# Author: Junchi Wang
# Date: 2024/3/9
# Version: v1.0

import numpy as np
import matplotlib.pyplot as plt

# Wavelet transform(convolution) function
def wavelet_transform(x, wavelet):
    n = len(x)
    m = len(wavelet)
    y = np.zeros(n)
    for i in range(n):
        for j in range(m):
            if i - j >= 0 and i - j < n:
                y[i] += wavelet[j] * x[i - j]
    return y

x = np.zeros(50)
x = np.append(x, np.ones(100))
x = np.append(x, np.zeros(100))
x = np.append(x, np.sin(np.linspace(0, 4 * np.pi, 200)))
noise = np.random.normal(0, 0.1, len(x))
x += noise
wavelet = np.array([1, -1])
y = wavelet_transform(x, wavelet)

plt.subplot(2, 1, 1)
plt.plot(x, label='x')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(y, label='y')
plt.legend()  

plt.show()