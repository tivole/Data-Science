# (c) Tivole

# Constanst
N = 100 # How many numbers you want to take

# Importing the libraries
import pandas as pd
import numpy as np

# Importing dataset
dataset = pd.read_csv('Random_Numbers.csv')

# Reading samples
X_1 = dataset.iloc[:N, 0].values
X_2 = dataset.iloc[:N, 1].values
X_3 = dataset.iloc[:N, 2].values
X_0 = np.ones((N,))

# Finding etta
etta = np.array([dataset.iloc[:N, 35 - 1].values]).T

# Finding X
X = np.array([X_0, X_1, X_2, X_3]).T

# Finding B
B = np.dot(X.T, X)

# tetta
_tetta_ = np.dot(np.dot((np.linalg.inv(B)), X.T), etta)

# Finding MSE of tetta
mean_tetta_ = sum(_tetta_)[0]

MSE_tetta = sum([(_tetta_[i][0] - mean_tetta_)**2 for i in range(4)]) / N
