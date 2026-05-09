import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



dataset = pd.read_csv("data.csv")

dataset = pd.DataFrame(dataset)

X = dataset[['YEAR', 'MO', 'DY', 'HR']]
Y = dataset['T2M']

model = LinearRegression()
model.fit(X, Y)


print(model.predict([[2046, 1, 3, 1]]))

