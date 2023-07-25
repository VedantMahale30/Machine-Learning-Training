import pandas as pd 
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("play_data_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

feature = data[["Weather"]]
nfeature = pd.get_dummies(feature) 
print(nfeature)
print(feature)
target =data["Play"]

model = BernoulliNB()
model.fit(nfeature,target)

we = int(input("1- Overcast , 2-Rainy , 3-Sunny"))
if we ==1:
	data =[[1,0,0]]
elif we == 2:
	data =[[0,1,0]]
else:
	data =[[0,0,1]]

ans  =  model.predict(data)
print(ans)
print(model.predict_proba(data))
















