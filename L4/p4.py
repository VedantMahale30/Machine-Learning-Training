import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("fqpsep2002.csv")
print(data)

features = [["name","quantity"]]
target =data["price"] 

model = LinearRegression()
model.fit(features , target)