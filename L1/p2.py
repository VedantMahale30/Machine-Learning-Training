import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("hp.csv")

feature = data[["area"]]
target = data["price"]


print(data)
print(feature)
print(target)

model=LinearRegression()
model.fit(feature , target)

area = float(input("Enter The Area Of bunglow"))
price = model.predict([[area]])
print("price = " ,price)