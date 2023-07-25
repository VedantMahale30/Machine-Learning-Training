#IMPORT LIB
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor

#load data
data = pd.read_csv("weight_data_sep2022.csv")
print(data)

#understand the data 
res =  data.isnull().sum()
print(res)

#features and target
features = data[["HEIGHT","AGE"]]
target = data["WEIGHT"]

#feature scalling 

mms = MinMaxScaler()
nfeatures =mms.fit_transform(features)
print(features)
print(nfeatures)

#find N
N= int(len(data)**0.5)
if N %2==0:
	N =N+1

#model and fit
model = KNeighborsRegressor(n_neighbors = N,metric="euclidean")
model.fit(nfeatures ,target)


#predict
ht  = float(input("Enter Height :"))
ag = float(input("Enter Age : "))
d = [[ht,ag]]
nd =mms.transform(d)
ans = model.predict(nd)
print(ans)


















