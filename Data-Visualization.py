import numpy as np 

import matplotlib.pyplot as plt

import math

plt.rcParams['figure.figsize'] = [4,3]

x_vals = np.linspace(0,20,20)
y_vals = [math.sqrt(i) for i in x_vals]
y2_vals = x_vals ** 3

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals, 'r' , label='Square Roots')
plt.plot(x_vals, y2_vals, 'b' , label='Cube')
plt.legend(loc = 'upper center')
plt.show()