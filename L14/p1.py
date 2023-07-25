import pandas as pd 
from sklearn.cluster import KMeans

#load data 
data = pd.read_csv("xy_data_sep2022.csv")
print(data)

#features only
features = data[["X","Y"]]

#model 
model = KMeans(n_clusters =2)

#clusters 
res = model.fit_predict(features)
print(res)
data["cluster"] = res
print(data)

#show centroid
print(model.cluster_centers_)


#predict 
x = float(input("Enter Value Of X "))
y = float(input("Enter Value of Y "))
ipdata = [[x,y]]
ans = model.predict(ipdata)
print(ans)

import matplotlib.pyplot as plt
plt.scatter(data["X"],data["Y"], c=data["cluster"])
plt.show()









