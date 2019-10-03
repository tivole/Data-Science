# (c) Tivole

# Constanst
N = 25 # Number of values

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv('clustering.csv')
A = dataset.iloc[:N, 0].values
B = dataset.iloc[:N, 1].values
C = dataset.iloc[:N, 2].values
D = dataset.iloc[:N, 3].values








# Visualising
plt.scatter(A, B, color = 'red')
plt.scatter(B, C, color = 'green')
plt.title('Statistics subject 13')
plt.xlabel('A')
plt.ylabel('B')
plt.show()