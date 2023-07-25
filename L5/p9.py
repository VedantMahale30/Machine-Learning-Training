import pandas as pd 
from sklearn.linear_model import LinearRegression 

data = pd.read_csv("temp_pressure_sep2022.csv")
print(data)

feature = data[["temp"]]
target = data["pressure"]

model = LinearRegression()
model.fit(feature ,target)

temp = float(input("Enter Temp : "))
pressure = model.predict([[temp]])
print("Pressure =" , pressure)