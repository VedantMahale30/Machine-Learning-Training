import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, classification_report
import matplotlib.pyplot as plt

data = pd.read_csv("titanic_data_sep2022.csv")
ndata = data.drop(["PassengerId","Name","Ticket","Cabin"], axis="columns")
print(ndata)

res = ndata.isnull().sum()
print(res)


nndata =ndata.fillna({
	"Age":ndata["Age"].mean(),
	"Embarked":"S"
	})

res = nndata.isnull().sum()
print(res)

#features and data 
features = nndata.drop("Survived",axis="columns")
target = nndata["Survived"]

#Handle cat data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#train test 
x_train,x_test,y_train,y_test = train_test_split(nfeatures , target)

#model and fit 
model = DecisionTreeClassifier()
mf = model.fit(x_train,y_train)

#performance
plot_confusion_matrix(model,x_test,y_test)
plt.show()
cr = classification_report(y_test,model.predict(x_test))
print(cr)

#predict
data = [[1,19.000000,0 ,0,30.0000,1, 0,0,0,1]]
ans = model.predict(data)
print(ans)








