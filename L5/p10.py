import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("temp_pressure_sep2022.csv")
print(data)

feature = data[["temp"]]
target = data["pressure"]

pf = PolynomialFeatures(degree = 5)
pfeature = pf.fit_transform(feature)

model = LinearRegression()
model.fit(pfeature ,target)

temp = float(input("Enter Temp : "))
ptemp = pf.fit_transform([[temp]])
pressure = model.predict(ptemp)
print("Pressure =" , pressure)