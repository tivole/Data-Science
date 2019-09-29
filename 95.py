# (c) Tivole

# Constanst
NUMBER_ON_TABLE = 7 # Your ID number on group list
N = 100 # How many number you want to take

# Importing the libraries
import pandas as pd
import numpy as np

# Importing dataset
dataset = pd.read_csv('Random_Numbers.csv')
Y = dataset.iloc[:N, NUMBER_ON_TABLE - 1].values
Y.sort()

# Distribution Function
F = lambda x: x**2
F_inv = lambda y: np.sqrt(y)

# Calculation Xs
X = np.array([F_inv(Y[i]) for i in range(len(Y))])

# Kolmagorov's criterion
max_val = max((1/N - X[0]), X[0])
for i in range(N):
    possible_max_val = max(((i+1)/N - X[i]), (X[i] - (i)/N))
    max_val = max(max_val, possible_max_val)

D_n = max_val
a = np.sqrt(N) * D_n

# Omega-square criterion
b = 1/(12*N)

for i in range(N):
    b += (X[i] - (2*(i+1) - 1)/(2*N))**2

