import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

data =  pd.read_csv("age_movie_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

feature = data[["age"]]
target = data["movie"]

model = LogisticRegression()
model.fit(feature,target)

age = float(input("Enter Age : "))
res = model.predict_proba([[age]])
print(res)


r =  res.ravel().tolist()
rddlj = round(r[0]*100,2);		print("DDLJ",rddlj)
rhp = round(r[1]*100,2);		print("HP",rhp)
rmh = round(r[2]*100,2);		print("MH",rmh)
rsil = round(r[3]*100,2);		print("Silsila",rsil)
