# (c) Tivole

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constanst
N = 8 # Dimention of cube

# Importing dataset
dataset = pd.read_csv('Random_Numbers.csv')
Y = dataset.iloc[:, :N].values

# Calculation frequence
ans = 0
for i in range(len(Y)):
    if sum([Y[i][j]**2 for j in range(N)]) <= 1.0:
        ans += 1

# Probability of hitting the ball
p_m = (np.pi/2)**(4) / (2*4*6*8)