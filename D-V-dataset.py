import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('iris.csv')

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal VS Petal Length')
plt.plot(data['SepalLengthCm'], data['PetalLengthCm'],'b')
plt.show()