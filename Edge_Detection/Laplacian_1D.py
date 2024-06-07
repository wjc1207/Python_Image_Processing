import matplotlib.pyplot as plt
import numpy as np

image = np.zeros(100)
image[50:75] = 255

def Laplacian(signal):
    grad = np.zeros(len(signal))
    for i in range(len(signal) - 1):
        grad[i] = signal[i+1] - signal[i]
    
    second_grad = np.zeros(len(grad))
    for i in range(len(grad) - 1):
        second_grad[i] = grad[i+1] - grad[i]
    
    return second_grad

grad_of_image = Laplacian(image)

plt.subplot(2,1,1)
plt.title('Original Image')
plt.plot(image)
plt.subplot(2,1,2)
plt.title('Second Gradient of Image')
plt.plot(grad_of_image)
plt.show()