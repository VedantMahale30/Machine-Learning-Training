import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

data = pd.read_csv("result_data_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

feature =data[["hr"]]
target =data["result"]

model  = DecisionTreeClassifier()
mf =model.fit(feature,target)

hr = float(input("Enter Hours : "))
res = model.predict([[hr]])
print(res)

plot_tree(mf,fontsize=10,filled=True,feature_names =["hr","hr"],class_names = ["FAIL","PASS"])
plt.show()


