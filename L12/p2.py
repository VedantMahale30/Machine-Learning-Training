#import lib 
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt

#load the data 
data = pd.read_csv("run_data_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

features = data[["Weather" , "Just Ate"]]
target = data["Will I Go Running?"]

nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#model and fit
model = DecisionTreeClassifier()
mf =model.fit(nfeatures ,target)

plot_tree(mf,fontsize=10,filled=True,feature_names =["Weather","Weather","Just Ate","Just Ate"],class_names = ["Nahi Jana Bhai","Chalo Chalo"])
plt.show()