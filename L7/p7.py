import pandas as pd
from sklearn.linear_model import LogisticRegression 

data = pd.read_csv("vehicle_data_sep2022.csv")
print(data)

feature =data[["Age"]]
target =data[["Vehicle"]]

model = LogisticRegression()
model.fit(feature,target)

age = float(input("Enter Age : " ))
res = model.predict_proba([[age]])
print(res)


r = res.ravel().tolist()
print(r)


rbike = r[0]*100;	print("Bike",round(rbike,2))
rcar = r[1]*100;	print("Car",round(rcar,2))
rcycle = r[2]*100;	print("Cycle",round(rcycle,2))

