import matplotlib.pyplot as plt
import numpy as np

def edge_detection_by_graident(image, threshold):
    # assume image is 2D
    edge_image = np.zeros(image.shape)
    image = image.astype(np.int16)
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            edge_image[i,j] = np.abs(image[i+1, j] - image[i,j]) + np.abs(image[i,j+1] - image[i,j])
            if edge_image[i,j] > threshold:
                edge_image[i,j] = 255
            else:
                edge_image[i,j] = 0

    return edge_image

def improved_edge_detection_by_graident(image, threshold):
    # assume image is 2D
    # add mean filter to eliminate noise
    edge_image = np.zeros(image.shape)
    image = image.astype(np.int16)
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            edge_image[i,j] = (np.abs(image[i+1,j+1] + image[i+1, j] + image[i+1, j-1] - image[i-1, j+1] - image[i-1, j] - image[i-1, j-1]) + np.abs(image[i+1,j+1] + image[i, j+1] + image[i-1, j+1] - image[i+1, j-1] - image[i, j-1] - image[i-1, j-1])) // 6
            if edge_image[i,j] > threshold:
                edge_image[i,j] = 255
            else:
                edge_image[i,j] = 0

    return edge_image

import cv2
image = cv2.imread('Image Processing/test.png', 0) # replace with your image
image = image + np.random.normal(0, 5, image.shape)
edge_image = improved_edge_detection_by_graident(image, 20)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1,2,2)
plt.title('Edge Image')
plt.imshow(edge_image, cmap='gray')
plt.show()