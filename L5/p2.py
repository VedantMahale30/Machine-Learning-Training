import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

#load 
data = pd.read_csv("place_area_price_sep2022.csv")
print(data) 
res = data.isnull().sum()
print(data)

features = data[["place","area"]]
target = data["price"]


ct = ColumnTransformer([("place",OneHotEncoder(),[0])], remainder ="passthrough")
tfeatures = ct.fit_transform(features)
print(tfeatures)

nfeatures = pd.DataFrame(tfeatures[:,:], columns =["Karjat","Khandala","Lonavala","area"])
print(nfeatures)



