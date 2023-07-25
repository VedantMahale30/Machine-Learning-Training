import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import plot_confusion_matrix,classification_report
import matplotlib.pyplot as plt

data = pd.read_csv("Social_Network_Ads_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

features = data[["Gender","Age","EstimatedSalary"]]
target = data["Purchased"]

nfeatures = pd.get_dummies(features)
print(nfeatures)

x_train,x_test,y_train,y_test = train_test_split(nfeatures , target)

model = GaussianNB()
model.fit(x_train,y_train)


plot_confusion_matrix(model,x_test,y_test)
plt.show()

input()

cr = classification_report(y_test,model.predict(x_test))
print(cr)


age =float(input("enter age"))
sal =float(input("enter salary"))
gen =int(input("1-female , 2-male")) 
if gen == 1:
	data=[[age , sal, 1,0]]
else :
	data =[[age, sal,0,1]]



ans = model.predict(data)
print(ans)
print(model.predict_proba(data))












