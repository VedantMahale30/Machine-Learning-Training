# import lib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, classification_report
import matplotlib.pyplot as plt

# load data

data = pd.read_csv("car_data_sep2022.csv")
data.columns = ["buying", "maintenence",  "doors", "persons", "luggage", "safety", "condition"]
print(data)


#checking null data 

res = data.isnull().sum()
print(res)

# feature target
features = data.drop("condition", axis="columns")
target = data["condition"]


# nfeature 
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)


#model and fit
model = DecisionTreeClassifier()
model.fit(nfeatures, target)


# feature importance
print(model.feature_importances_)
x = nfeatures.columns
y = model.feature_importances_
plt.figure(figsize=(10, 5))
plt.barh(x,y)
plt.ylabel("feature names")
plt.xlabel("Importance")
plt.show()



