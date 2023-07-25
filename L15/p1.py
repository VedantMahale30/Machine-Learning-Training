import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

#load the data
data = pd.read_csv("Mall_Customers_sep2022.csv")
print(data)

#understand the data
print(data.shape)
res = data.isnull().sum()
print(res)

#features 
features =data[["Annual_Income","Spending_Score"]]

#features scalling 
mms = MinMaxScaler()
nfeatures = mms.fit_transform(features)
print(features)
print(nfeatures)

#model 
model = KMeans(n_clusters =5,random_state=123)

#fit_predict
res = model.fit_predict(nfeatures)
data["cluster"] =res
print(data)


#sep the clusters
data0 =data[data.cluster == 0]
data1 =data[data.cluster == 1]
data2 =data[data.cluster == 2]
data3 =data[data.cluster == 3]
data4 =data[data.cluster == 4]




plt.scatter(data0["Annual_Income"],data0["Spending_Score"],color = "red",label="MI MS")
plt.scatter(data1["Annual_Income"],data1["Spending_Score"],color = "blue",label="HI Hs")
plt.scatter(data2["Annual_Income"],data2["Spending_Score"],color = "green",label="HI LS")
plt.scatter(data3["Annual_Income"],data3["Spending_Score"],color = "brown",label="LI LS")
plt.scatter(data4["Annual_Income"],data4["Spending_Score"],color = "orange",label="LI HS")
plt.legend()
plt.show()


#predict
AI = float(input("Enter Annual Income"))
SS = float(input("Enter Total Spending Score"))
d = [[AI,SS]]
ans = model.predict(d)
if ans == 0:
	print("MI MS")
elif ans ==1:
	print("HI HS")
elif  ans == 2:
	print("HI LS")
elif  ans == 3:
	print("LI LS")
else :
	print("LI HS")
print(ans)


















