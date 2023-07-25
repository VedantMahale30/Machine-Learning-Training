import pandas as pd 
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("go_sh_data_sep2022.csv")
print(data)

res= data.isnull().sum()
print(res)

features = data[["Weather","Car"]]
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

target = data["Result"]

model = BernoulliNB()
model.fit(nfeatures ,target)

we = int(input("1- Rainy, 2-sunny"))
ca = int(input("1- broken ,2-working"))
if we ==1 and ca==1:
	data=[[1,0,1,0]]
elif we ==1 and ca ==2:
	data = [[1,0,0,1]]
elif we ==2 and ca ==1:
	data = [[0,1,1,0]]
else:	
	data = [[0,1,0,1]]

ans = model.predict(data)
print(ans)
print(model.predict_proba(data))

