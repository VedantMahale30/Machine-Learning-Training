import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("pos_sal_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

feature = data[["Level"]]
target = data["Salary"]

pf = PolynomialFeatures(degree=4)
pfeature =pf.fit_transform(feature)

model= LinearRegression()
model.fit(pfeature , target)

level = float(input("Enter Level : "))
plevel = pf.fit_transform([[level]])
salary = model.predict(plevel)
print("Salary : ",salary)

