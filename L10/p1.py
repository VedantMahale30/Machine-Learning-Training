import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

data= pd.read_csv("tshirt_data_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

features = data[["Height(cm)","Weight(kg)"]]
target = data["T-Shirt Size"]

mms= MinMaxScaler()
nfeatures = mms.fit_transform(features)
print(features)
print(nfeatures)

N= int(len(data)**0.5)
if N % 2 ==0:
	N = N+1

model = KNeighborsClassifier(n_neighbors = 3,metric="euclidean")
model.fit(nfeatures ,target)

ht = float(input("Enter Height :"))
wt = float(input("Enter Weight :"))
data = [[ht , wt]]
ndata = mms.transform(data)
ans = model.predict(ndata)
print(ans)

ne = model.kneighbors(ndata,n_neighbors = N)
print(ne)

