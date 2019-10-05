# (c) Tivole

# Constanst
NUMBER_ON_TABLE = 7 # Your ID number on group list
N = 100 # How many numbers you want to take

# Importing the libraries
import pandas as pd
import numpy as np

# Importing dataset
dataset = pd.read_csv('Random_Numbers.csv')

# First Sample
X = list(dataset.iloc[:N, 35 - 1].values)
X = [[X[i], i] for i in range(len(X))]

X_new = X[:]
X_new.sort(key=lambda x: x[0])

for i in range(N):
    X[X_new[i][1]][1] = i + 1
del(X_new)


# Second Sample
Y = list(dataset.iloc[:N, NUMBER_ON_TABLE - 1].values)
Y = [[Y[i], i] for i in range(len(Y))]

Y_new = Y[:]
Y_new.sort(key=lambda x: x[0])

for i in range(N):
    Y[Y_new[i][1]][1] = i + 1
del(Y_new)

_ro_s = 1 - (6/(N**3 - N))*sum([(X[i][1] - Y[i][1])**2 for i in range(N)]) 


def K(x): 
    sum = 0 
    for k in range(-100, 100): 
        sum += (-1)**k*np.exp(-2*k**2*x**2) 
    return 1 - sum 
