import matplotlib.pyplot as plt
import numpy as np

def edge_detection_by_Laplacian(image, threshold):
    # assume image is 2D
    Laplacian_image = np.zeros(image.shape)
    edge_image = np.zeros(image.shape)
    image = image.astype(np.int16)
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            Laplacian_image[i,j] = image[i+1,j] + image[i-1,j] + image[i,j+1] + image[i,j-1] - 4*image[i,j]

    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            if Laplacian_image[i+1,j] * Laplacian_image[i-1,j] < -threshold or Laplacian_image[i,j+1] * Laplacian_image[i,j-1] < -threshold:
                edge_image[i,j] = 255
            else:
                edge_image[i,j] = 0

    return edge_image

import cv2
image = cv2.imread('Image Processing/test.png', 0) # replace with your image
edge_image = edge_detection_by_Laplacian(image, 40)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1,2,2)
plt.title('Edge Image')
plt.imshow(edge_image, cmap='gray')
plt.show()