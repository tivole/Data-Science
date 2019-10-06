# (c) Tivole

# Constanst
NUMBER_ON_TABLE = 7 # Your ID number on group list
N = 100 # How many numbers you want to take

# Importing the libraries
import pandas as pd
import numpy as np

# Importing dataset
dataset = pd.read_csv('Random_Numbers.csv')

# Calculating Xs
X = [((i+1)/N) for i in range(N)]

# Calculating Ys
Y = dataset.iloc[:N, NUMBER_ON_TABLE - 1].values
Y = [(X[i] + (Y[i] - 0.5)) for i in range(N)]

# Calculating b
b = []
for i in range(N-1):
    for j in range(i+1, N):
        b.append((Y[j] - Y[i]) / (X[j] - X[i]))

b.sort()

B = (b[int(N*(N-1)/4 - 1)] + b[int(N*(N-1)/4)]) / 2

# Calculating a
a = []
for i in range(N):
    a.append(Y[i] - B * X[i])

a.sort()

A = (a[int(N/2 - 1)] + a[int(N/2)]) / 2

print(A, B)