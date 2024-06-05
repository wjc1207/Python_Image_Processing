import matplotlib.pyplot as plt
import numpy as np

image = np.zeros(100)
image[50:75] = 255

def gradient(signal):
    grad = np.zeros(len(signal))
    for i in range(len(signal) - 1):
        grad[i] = np.abs(signal[i+1] - signal[i])
    
    return grad

grad_of_image = gradient(image)

plt.subplot(2,1,1)
plt.title('Original Image')
plt.plot(image)
plt.subplot(2,1,2)
plt.title('Gradient of Image')
plt.plot(grad_of_image)
plt.show()