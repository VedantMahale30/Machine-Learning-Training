import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("pos_sal_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

feature = data[["Level"]]
target = data["Salary"]

model= LinearRegression()
model.fit(feature , target)

level = float(input("Enter Level : "))
salary = model.predict([[level]])
print("Salary : ",salary)

