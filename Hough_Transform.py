import numpy as np
import matplotlib.pyplot as plt

# Hough Transform

# Generate some data
x = np.arange(0, 120, 1)
line1 = 0.5 * x + 10
line2 = - 2 * x + 20
data = np.column_stack((x, line1))
data = np.vstack((data, np.column_stack((x, line2))))

hough_space = np.zeros((60,64))


for n in range(len(data)):
    for z in np.arange(-30,30,1):
        for theta in np.arange(0,np.pi,0.05):
            if (abs(data[n,0]*np.sin(theta) - data[n,1]*np.cos(theta) + z) < 0.2): # quantization error
                hough_space[z+30,int(theta*20)] += 1 # streth the theta axis by 20
 


plt.figure()
plt.imshow(hough_space)
# show x and y axis
plt.colorbar()
plt.axhline(y=30, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.title('Hough Space')
plt.xlabel('Theta')
plt.ylabel('Z')
plt.show()








