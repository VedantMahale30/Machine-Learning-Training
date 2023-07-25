#import lib 
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt

#load the data 
data = pd.read_csv("loan_default_data_Sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

features = data[["GENDER","OCCUPATION"]]
target = data["DEFAULT"]

nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#model and fit
model = DecisionTreeClassifier()
mf =model.fit(nfeatures ,target)

plot_tree(mf,fontsize=10,filled=True,feature_names =["GENDER","GENDER","OCCUPATION","OCCUPATION"],class_names = ["no","yes"])
plt.show()