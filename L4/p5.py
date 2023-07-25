import pandas as pd 
from sklearn.linear_model import LinearRegression

data= pd.read_csv("fqpsep2002.csv")
print(data)

res = data.isnull().sum()
print(res)

#handle the null data 
ndata = data.fillna({"name":"Mango","price":6.5})
print(ndata)

#handle the cat data 
dummies = pd.get_dummies(ndata.name)
print(dummies)

fdata = pd.concat([ndata,dummies],axis="columns")
print(fdata)


features =fdata[["quantity","Apple","Mango"]] 
target =fdata["price"]

model = LinearRegression()
model.fit(features , target)

qty = int(input("Enter Qty : "))
name = int(input("1- Apple ,  2-Mango"))

if name == "1":
	data = [[qty,1,0]]
else:
	data = [[qty,0,1]]

price= model.predict(data)
print(price)







