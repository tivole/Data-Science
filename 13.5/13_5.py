# (c) Tivole

# Constanst
N = 25 # Number of values

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Importing dataset
dataset = pd.read_csv('clustering.csv')
A = dataset.iloc[:N, 0].values
B = dataset.iloc[:N, 1].values
C = dataset.iloc[:N, 2].values
D = dataset.iloc[:N, 3].values

# Visualising
plt.scatter(A, B, color = 'red', label = '(A, B)')
plt.scatter(B, C, color = 'green', label = '(B, C)')
plt.title('Statistics subject 13')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

X = np.array([A, B]).T

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 4)
y_kmeans = kmeans.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 40, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 40, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 40, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 40, c = 'cyan', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 50, c = 'yellow', label = 'Centroids')
plt.title('Statistics home work')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()