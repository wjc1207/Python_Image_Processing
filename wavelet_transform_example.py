# Wavelet transform example
# sudden edge detection
# Author: Junchi Wang
# Date: 2024/07/21
# Version: v1.1

import numpy as np
import matplotlib.pyplot as plt

# Wavelet transform(convolution) function
def wavelet_transform(x, wavelet):
    n = len(x)
    m = len(wavelet)
    y = np.zeros(n,dtype=np.complex_)
    for i in range(n):
        for j in range(m):
            if i - j >= 0 and i - j < n:
                y[i] += wavelet[j] * x[i - j]
    return y

delta = 0.1
N = 100
# generate sine wave with increasing frequency
x = np.array(np.sin(np.arange(0, N * delta, delta)))
delta_values = np.arange(0.2, 1, 0.1)
for delta in delta_values:
    x = np.append(x, np.array(np.sin(np.arange(0, N * delta, delta))))
# Morlet wavelet
wavelet_delta = 0.6
wavelet = np.exp(1j*np.arange(-N * wavelet_delta / 2, N * wavelet_delta / 2, wavelet_delta)) * np.exp(-np.power(np.arange(-N / 2, N / 2)/30,2)/2)
y = wavelet_transform(x, wavelet)

# plot
plt.subplot(3, 1, 1)
plt.plot(x, label='x')
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(wavelet, label = "wavelet")
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(abs(y), label='y')
plt.legend()  

plt.show()