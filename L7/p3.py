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
b0 = model.intercept_
b1 = model.coef_
num = 1 
den = 1+2.71**-(b0+b1*age)
hi = num/den
print(hi)

if hi >0.5:
	print("Yes")
else:
	print("No")


