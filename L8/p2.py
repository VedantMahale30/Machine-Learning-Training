
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
mo = model.predict([[age]])
print(mo)