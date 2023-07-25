import pandas as pd 
from sklearn.linear_model import LinearRegression 
data = pd.read_csv("papsep2022.csv")

features = data[["place","area"]]
target = data["price"]

print(features)
print(target)

model = LinearRegression()
model.fit(features , target)