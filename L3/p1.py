import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("pets.csv")
print(data)

features = data[["exp","test"]]
target = data["salary"]

model=LinearRegression()
model.fit(features,target)

exp = float(input("Enter Experience = "))
test = float(input("Enter Test Scr = "))
salary = model.predict(features ,target)

print("Salary IS -",salary)


b0= model.intercept_
b1 = model.coef_[0]
b2 = model.coef_[1]

nsalary = b0 +   b1*exp  +  b2*test
print("nsalary = ", nsalary)
