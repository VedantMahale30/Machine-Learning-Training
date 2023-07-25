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
b0 = model.intercept_
b1 = model.coef_

price = b0 + b1*area
#Y    = c  + m *  x

print("price = " ,price)