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

omega = 0.1
N = 100
x = np.array(np.sin(np.arange(0, N * omega, omega)))
omega_values = np.arange(0.2, 1, 0.1)
for omega in omega_values:
    x = np.append(x, np.array(np.sin(np.arange(0, N * omega, omega))))
wavelet_omega = 0.5
wavelet = np.sin(np.arange(-N * wavelet_omega / 2, N * wavelet_omega / 2, wavelet_omega)) * np.exp(-np.power(np.arange(-N / 2, N / 2)/20,2)/2)
y = wavelet_transform(x, wavelet)

plt.subplot(3, 1, 1)
plt.plot(x, label='x')
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(y, label='y')
plt.legend()  
plt.subplot(3, 1, 3)
plt.plot(wavelet, label = "wavelet")
plt.legend()

plt.show()