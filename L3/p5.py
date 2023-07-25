# find na and drop na


import pandas as pd 
from sklearn.linear_model import LinearRegression

data = pd.read_csv("apple.csv")
print(data)

res = data.isnull().sum()
print(res)

ndata = data.fillna({"price":data["price"].mean()})

print(data)
print(ndata)

feature = ndata[["qty"]]
target = ndata["price"]

model =LinearRegression()
model.fit(feature,target)

qty = float(input("Enter Qty"))
price = model.predict([[qty]])
print("Price= ",price)