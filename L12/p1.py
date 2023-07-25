import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("run_data_sep2022.csv")
print(data)

#understand the data 
res = data.isnull().sum()
print(res)

#features and target 
features = data[["Weather" , "Just Ate"]]
print(features)
target  = data["Will I Go Running?"]

#Handle Cat Data 
nfeatures = pd.get_dummies(features)
print(nfeatures)

#model and fit 
model = DecisionTreeClassifier()
model.fit(nfeatures,target)

#predict 
we = int(input("1 Sunny ---- 2 for Rainy "))
if we == 1:
	data = [0,1]
else:
	data = [1,0]
ate = int(input("1 for YES ----2 for No "))
if ate ==1:
	data.extend([0,1])
else: 
	data.extend([1,0])

ans = model.predict([data])
print(ans)