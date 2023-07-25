import pandas as pd 
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("result_data_sep2022.csv")
print(data)

feature= data[["hr"]]
target = data["result"]

model =  LogisticRegression()
model.fit(feature ,target)

hr =  float( input("Enter Hours :"))
result = model.predict([[hr]])
print(result)