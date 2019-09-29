# (c) Tivole

# Constanst
NUMBER_ON_TABLE = 7 # Your ID number on group list
N = 100 # How many numbers you want to take as "First Sample"
M = 100 # How many numbers you want to take as "Second Sample"

# Importing the libraries
import pandas as pd
import numpy as np

# Importing dataset
dataset = pd.read_csv('Random_Numbers.csv')

# Distribution Functions
F = lambda x: 1 - np.exp(-x)
F_inv = lambda y: - np.log(1 - y)
G = lambda x: 1 - np.exp(-x + 0.2)
G_inv = lambda y: 0.2 - np.log(1 - y)

# First Sample
X = dataset.iloc[:N, 35 - 1].values
X.sort()
X = np.array([F_inv(X[i]) for i in range(len(X))])

# Second Sample
Y = dataset.iloc[:M, NUMBER_ON_TABLE - 1].values
Y.sort()
Y = np.array([G_inv(Y[i]) for i in range(len(Y))])

# Calculation mean_X and mean_Y
mean_X = sum(X) / len(X)
mean_Y = sum(Y) / len(Y)

# Calculating S_1^2 and S_2^2
S_1_sqr = sum([(X[i] - mean_X)**2 for i in range(len(X))]) / (len(X) - 1)
S_2_sqr = sum([(Y[i] - mean_Y)**2 for i in range(len(Y))]) / (len(Y) - 1)

# Calculating S_tot^2
S_tot_sqr = ((N - 1)*S_1_sqr + (M - 1)*S_2_sqr) / (N + M - 2)
S_tot = np.sqrt(S_tot_sqr)

# Calculating T
T = np.sqrt(N*M/(N + M)) * (mean_Y - mean_X) / S_tot