import cv2

# Load the image
image = cv2.imread("Image Processing/test.png")

# width, weight, and channel
width, height, channel = image.shape

import matplotlib.pyplot as plt
import numpy as np

N = 1000

plt.figure()
plt.plot(image[N,:,0])

signal = np.zeros(len(image[100,:,0]))

for i in range(1,len(image[100,:,0])-1):
    signal[i] = int(image[N,i+1,0]) - int(image[N,i-1,0])

for i in range(1,len(image[100,:,0])-1):
    signal[i] = signal[i+1] - signal[i]

edge = np.zeros(len(image[100,:,0]))
gaussion = np.exp(-np.arange(-10,11,1)**2/10)
signal = np.convolve(signal, gaussion, mode='same')
threshold = 20

for i in range(1,len(image[100,:,0])-1):
    if (signal[i-1] * signal[i+1] < -threshold**2) or (signal[i]*signal[i-1] < -threshold**2):
        edge[i] = 255
    else:
        edge[i] = 0

plt.plot(edge)
plt.plot(signal)
plt.show()
