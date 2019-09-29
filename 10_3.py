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

# First Sample
X = list(dataset.iloc[:N, 35 - 1].values)
X = [[X[i], 'X'] for i in range(len(X))]

# Distribution Function
G = lambda x: x**3
G_inv = lambda y: y**(1/3)

# Second Sample
Y = list(dataset.iloc[:M, NUMBER_ON_TABLE - 1].values)
Y = [G_inv(Y[i]) for i in range(len(Y))]
Y = [[Y[i], 'Y'] for i in range(len(Y))]

# Calculating S
S_all = X + Y
S_all.sort(key=lambda x: x[0])

k = 0
S = []
for i in range(len(S_all)):
    if S_all[i][1] == 'Y':
        S.append(i+1)

# Calculating V
V = sum(S)

# Calculating U {formula (5)}
U = V - M*(M + 1)/2

# Calculating MU and DU {forumula (6)}
MU = N*M/2
DU = N*M*(N + M + 1)/12

# Calculating U* {formula (7)}
U_star = (U - MU)/np.sqrt(DU)