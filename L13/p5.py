# import lib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, classification_report
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("car_data_sep2022.csv")
data.columns = ["buying", "maintenence",  "doors", "persons", "luggage", "safety", "condition"]
print(data)
data.drop(["buying", "maintenence",  "doors", "luggage"],axis ="columns",inplace= True)

#checking null data 
res =data.info()
print(res)
res = data.isnull().sum()
print(res)

# feature target
features = data.drop("condition", axis="columns")
target = data["condition"]



# nfeature  Handle cat data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#train test
x_train,x_test,y_train,y_test=train_test_split(nfeatures,target)



#model and fit
model = RandomForestClassifier()
model.fit(x_train,y_train)


#classifier report
cr = classification_report(y_test,model.predict(x_test))
print(cr)


#predict

data= [[1,0,0,0,0,1]]
data = [[0,0,1,1,0,0]]
ans = model.predict(data)
print(ans)
