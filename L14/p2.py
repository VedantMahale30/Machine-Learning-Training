#import Library
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

#read data
data = pd.read_csv("ab_data_sep2022.csv")
print(data)

#understand the data 

#features
features = data[["A","B"]]

#model 
model = KMeans(n_clusters=3)

#fit predict 
res = model.fit_predict(features)
data["clusters"] = res
print(data) 

# centroid 
print(model.cluster_centers_)

#predict
a = float(input("Enter Value Of A "))
b = float(input("Enter Value of B "))
d = [[a,b]]
ans = model.predict(d)
print(ans)

import matplotlib.pyplot as plt
plt.scatter(data["A"],data["B"], c=data["clusters"])
plt.show()
















