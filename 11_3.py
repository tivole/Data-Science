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
Y_1 = dataset.iloc[:N, (NUMBER_ON_TABLE - 1) - 1].values # 6 column
Y_2 = dataset.iloc[:N, (NUMBER_ON_TABLE - 1)].values # 7 column
Y_3 = dataset.iloc[:N, (NUMBER_ON_TABLE - 1) + 1].values # 8 column

# Modeling with Distribution Function x^3
X = np.array([max(Y_1[i], Y_2[i], Y_3[i]) for i in range(N)])
X.sort()

# Calculating MED
MED_X = (X[N//2 - 1] + X[N//2])/2 if N % 2 == 0 else X[N//2]

# Finding ksi and eta
ksi = np.array([(MED_X - X[i]) for i in range(N//2)])
eta = np.array([(X[N-i-1] - MED_X) for i in range(N//2)])

# Visualising the Training set results
plt.scatter(ksi, eta, color = 'red')
x = np.linspace(0, 1, 2)
plt.plot(x, np.sin(x))
plt.title('Statistics subject 11')
plt.xlabel('ksi')
plt.ylabel('eta')
plt.show()
