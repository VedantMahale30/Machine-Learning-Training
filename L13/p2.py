#import Lib 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix,classification_report

#load data
data = pd.read_csv("titanic_data_sep2022.csv")
data.drop(["PassengerId","Name","Ticket","Cabin","Parch","SibSp","Embarked"], axis="columns",inplace = True)
print(data.head())

#understaand the data 
res =data.isnull().sum()
print(res)

#handle null data
data.fillna({
	"Age":data["Age"].mean(),
	"Embarked":"S"
},inplace=True)
res = data.isnull().sum()
print(res)


#features n target
features = data.drop("Survived",axis="columns")
target = data["Survived"]

#handle cat data 
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#train and test 
x_train,x_test,y_train,y_test = train_test_split(nfeatures,target)

#model 
model = DecisionTreeClassifier()
model.fit(x_train,y_train)

#performance 
plot_confusion_matrix(model,x_test,y_test)
plt.show()
cr = classification_report(y_test,model.predict(x_test))
print(cr)

#predict 
data = [[1,35.000000,53.1000 ,1,0]]
ans = model.predict(data)
print(ans)












