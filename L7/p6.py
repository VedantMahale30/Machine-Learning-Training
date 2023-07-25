import pandas as pd
from sklearn.linear_model import LogisticRegression 
import matplotlib.pyplot as plt

data = pd.read_csv("vehicle_data_sep2022.csv")
print(data)

feature =data[["Age"]]
target =data[["Vehicle"]]

model = LogisticRegression()
model.fit(feature,target)

age = float(input("Enter Age: "))
veh = model.predict([[age]])
print(veh)