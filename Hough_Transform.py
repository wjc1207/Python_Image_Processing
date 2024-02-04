import numpy as np
import matplotlib.pyplot as plt

# Hough Transform

# Generate some data
x = np.arange(0, 120, 1)
line1 = 0.5*x + 10
line2 = - 2*x + 20
data = np.column_stack((x, line1))
data = np.vstack((data, np.column_stack((x, line2))))

hough_space = np.zeros((60, 60))


for n in range(len(data)):
    for i in np.arange(0, np.pi, 0.01):
        for j in range(-30,30):
            if (abs(data[n,0]*np.sin(i) - data[n,1]*np.cos(i) + j) < 0.1): # quantization error
                hough_space[int(i*10), j+30] += 1
 


plt.figure()
plt.imshow(hough_space)
plt.show()








