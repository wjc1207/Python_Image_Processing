import matplotlib.pyplot as plt
import numpy as np

def edge_detection_by_Canny(image, upper_threshold, lower_threshold):
    # assume image is 2D
    Laplacian_image = np.zeros(image.shape)
    strong_edge_image = np.zeros(image.shape)
    weak_edge_image = np.zeros(image.shape)
    image = image.astype(np.int16)
    smoothed_image = np.zeros(image.shape)
    Gaussian_kernel = np.array([[3,4,3],[4,5,4],[3,4,3]]) / 33
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            smoothed_image[i,j] = np.sum(image[i-1:i+2, j-1:j+2] * Gaussian_kernel)
    
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            Laplacian_image[i,j] = smoothed_image[i+1,j] + smoothed_image[i-1,j] + smoothed_image[i,j+1] + smoothed_image[i,j-1] - 4*smoothed_image[i,j]

    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            if Laplacian_image[i+1,j] * Laplacian_image[i-1,j] < -upper_threshold or Laplacian_image[i,j+1] * Laplacian_image[i,j-1] < -upper_threshold:
                strong_edge_image[i,j] = 255
            else:
                strong_edge_image[i,j] = 0
        
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            if Laplacian_image[i+1,j] * Laplacian_image[i-1,j] < -lower_threshold or Laplacian_image[i,j+1] * Laplacian_image[i,j-1] < -lower_threshold:
                weak_edge_image[i,j] = 255
            else:
                weak_edge_image[i,j] = 0

    for i in range(20):
        for j in range(image.shape[0] - 1):
            for k in range(image.shape[1] - 1):
                if weak_edge_image[j,k] == 255:
                    if strong_edge_image[j+1,k] == 255 or strong_edge_image[j-1,k] == 255 or strong_edge_image[j,k+1] == 255 or strong_edge_image[j,k-1] == 255 or strong_edge_image[j+1,k+1] == 255 or strong_edge_image[j-1,k-1] == 255 or strong_edge_image[j+1,k-1] == 255 or strong_edge_image[j-1,k+1] == 255:
                        strong_edge_image[j,k] = 255
                        weak_edge_image[j,k] = 0
    return strong_edge_image
 
import cv2
image = cv2.imread('Image Processing/test.png', 0) # replace with your image
edge_image = edge_detection_by_Canny(image, 40, 80)
edge_image += np.random.normal(0, 5, edge_image.shape)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1,2,2)
plt.title('Edge Image')
plt.imshow(edge_image, cmap='gray')
plt.show()