import pandas as pd 
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("email_data_sep2022.csv")
print(data.head())

res = data.isnull().sum()
print(res)
features =data[["Dear","Friend","Lunch","Money"]]
target = data["Result"]


nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)


model = BernoulliNB()
model.fit(nfeatures, target)


d = int(input("Dear: 1-No and 2-Yes"))
if d ==1:
	data=[1,0]
else:
	data=[0,1]

f = int(input("Friend :  1-No and 2-Yes"))
if f == 1:
	data.extend([1,0])
else:
	data.extend([0,1])


l  = int(input("Lunch :  1-No and 2-Yes"))
if l == 1:
	data.extend([1,0])
else:
	data.extend([0,1])


m = int(input("Money :  1-No and 2-Yes"))
if m == 1:
	data.extend([1,0])
else:
	data.extend([0,1])

ans =  model.predict([data])
print(ans)
res = model.predict_proba([data])


r = res.ravel().tolist()
r_normal = round(r[0]*100,2)
print("Normal",r_normal)
r_spam = round(r[1]*100,2)
print("Spam",r_spam)








