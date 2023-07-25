import pandas as pd
from sklearn.linear_model import LinearRegression


#Handle the null Data
from sklearn.impute import SimpleImputer
import numpy as np


#Handle cat data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


#check for Null data 
data = pd.read_csv("fqpsep2002.csv")
print(data)
res = data.isnull().sum()
print(res)


#handle null data 
imp1 = SimpleImputer(missing_values = np.nan,strategy="constant",fill_value="Mango")
data["name"] = imp1.fit_transform(data[["name"]])
print(data)

imp2 = SimpleImputer(missing_values = np.nan,strategy="constant",fill_value=6.5)
data["price"] = imp2.fit_transform(data[["price"]])
print(data)

#handle Cat data
features = data[["name","quantity"]]
ct = ColumnTransformer([("name",OneHotEncoder(),[0])], remainder ="passthrough")
tfeatures = ct.fit_transform(features)
print(features)
print(tfeatures)


nfeatures=pd.DataFrame(tfeatures[:,0:],
columns=["Apple","Mango","quantity"])
print(nfeatures)

#Features and target
target = data["price"]

model = LinearRegression()
model.fit(nfeatures , target)

name = int(input("1- Apple ,  2-Mango"))
qty = int(input("Enter Qty : "))

if name == 1:
	data = [[1,0 ,qty]]
else:
	data = [[0,1,qty]]

price= model.predict(data)
print(price)
















