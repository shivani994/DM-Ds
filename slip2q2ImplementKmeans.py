#ass6setbq1 slip2q2
# write python program to implement k- means algorithm on a synthetic dataset
# importing necessary libraries

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

# generating random data points
x, y = make_blobs(n_samples=100, centers=3, n_features=2)

# plotting the generated data points
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='gist_rainbow')
plt.show()
# implementing K-Means
k = 3

# assigning random centers
center = 10*np.random.rand(k, 2)
# computing the distance matrix
dist_matrix = np.zeros((100, 3))

for i in range(k):
 dist_matrix[:,i] = np.sum((x-center[i, :])**2, axis=1)

# assigning labels to each data point
cluster_labels = np.argmin(dist_matrix, axis=1)

# plotting the labeled data points
plt.scatter(x[:, 0], x[:, 1], c=cluster_labels, cmap='gist_rainbow')
plt.show()

# updating the cluster centers
for i in range(k):
 center[i, :] = np.mean(x[cluster_labels == i, :], axis=0)

# recomputing the distance matrix
dist_matrix = np.zeros((100, 3))

for i in range(k):
 center[i, :] = np.mean(x[cluster_labels == i, :], axis=0)

# recomputing the distance matrix
dist_matrix = np.zeros((100, 3))

for i in range(k):
 dist_matrix[:,i] = np.sum((x-center[i, :])**2, axis=1)

# reassigning labels to each data point
cluster_labels = np.argmin(dist_matrix, axis=1)

# plotting the labeled data points
plt.scatter(x[:, 0], x[:, 1], c=cluster_labels, cmap='gist_rainbow')
plt.show()
