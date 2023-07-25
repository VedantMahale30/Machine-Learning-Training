#import lib
import pandas as pd
from sklearn.cluster import KMean	s
from sklearn.preprocessing import MinMaxScaler

#load data
data = pd.read_csv("cricketers_data_sep2022.csv")
print(data)

#features
features = data[["RUNS","WICKETS"]]

#features scalling
mms = MinMaxScaler()
nfeatures = mms.fit_transform(features)
print(nfeatures)

#model 
model = KMeans(n_clusters=2 ,random_state = 123)

#fit predict
res = model.fit_predict(nfeatures)
data["clusters"] = res
print(data) 

# centroid 
print(model.cluster_centers_)

#predict
runs = float(input("Runs "))
wickets = float(input("Wickets "))
d = [[runs,wickets]]
nd = mms.transform(d)
ans = model.predict(nd)

if ans == 1 :
	print("Batsman ")
else:
	print("Bowler")


import matplotlib.pyplot as plt
plt.scatter(data["RUNS"],data["WICKETS"], c=data["clusters"])
plt.show()
