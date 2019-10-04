# (c) Tivole

# Constanst
NUMBER_ON_TABLE = 7 # Your ID number on group list
N = 20 # How many numbers you want to take as Sample

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv('Random_Numbers.csv')

# Modeling random values
Y = dataset.iloc[:N, (NUMBER_ON_TABLE - 1)].values
A = Y[:10]
B = Y[10:]


P = np.array([[A[i], B[i]] for i in range(N//2)])


# Visualising the Training set results
plt.scatter(A, B, color = 'red')
plt.title('Statistics subject 13')
plt.xlabel('A')
plt.ylabel('B')
plt.show()
