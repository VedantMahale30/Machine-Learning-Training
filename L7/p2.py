import pandas as pd
from sklearn.linear_model import LogisticRegression


data = pd.read_csv("insurance_data_sep2022.csv")
print (data)
print(data.head())

res = data.isnull().sum()
print(res)

feature = data[["age"]]
target = data["have_insurance"]

model = LogisticRegression()
model.fit(feature , target )

age = float(input("Enter Age : "))
hi  = model.predict([[age]])
print(hi)




