# K-means

import numpy as np
import matplotlib.pyplot as plt

data_point = np.array([[1,1],[2,2],[3,3],[1,2],[2,1],[9,9],[9,10],[10,9],[10,10],[9,9.5],[4,6],[4,4],[5,7]])

N = 2

iteration_num = 8

centriod = np.random.rand(N,2)*10

def compute_distance(x0, x1):
    distance = np.sqrt((x0 - x1).T @ (x0 - x1))
    return distance



for iter in range(iteration_num):
    data_cluster = [[] for _ in range(N)]
    for i in range(len(data_point)):
        distances = []
        for j in range(len(centriod)):
            distances.append(compute_distance(data_point[i],centriod[j]))
        index = np.argmin(distances)
        data_cluster[index].append(data_point[i])
    plt.figure()
    for k in range(len(data_cluster)):
        centriod[k] = np.mean(data_cluster[k])
        cluster = np.array(data_cluster[k])
        plt.scatter(cluster[:,0],cluster[:,1])
    
    plt.scatter(centriod[:,0],centriod[:,1], marker="*")
    plt.show()
    print(data_cluster)
    print(centriod)
    



    



