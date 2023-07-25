#Lib
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

#Load the data 
data = pd.read_csv("health_data_sep2022.csv")
print(data)

#Understand the data
res = data.isnull().sum()
print(res)

#feature and target 
features =data[["Weight","Height"]]
target = data["Class"]

#feature scalling 
mms= MinMaxScaler()
nfeatures = mms.fit_transform(features)
print(features)
print(nfeatures)

#find value of N 
N = int(len(data)**0.5)

if N % 2==0:
	N = N+1


#model and Fit 
model = KNeighborsClassifier(n_neighbors = N,metric="euclidean")
model.fit(nfeatures,target)

#predict
wt = float(input("Enter Weight: "))
ht = float(input("Enter Height: "))

data = [[ht,wt]]
ndata = mms.transform(data)
ans = model.predict(ndata)
print(ans)


ne = model.kneighbors(ndata,n_neighbors = N)
print(ne)











