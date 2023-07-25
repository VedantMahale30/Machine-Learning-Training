import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import plot_confusion_matrix,classification_report
import matplotlib.pyplot as plt

#load data 
data=pd.read_csv("diabetes_sep2022.csv")
print(data.head(10))

#convert 0 to nan
data[["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]] = data[["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]].replace(0,np.NAN)


# understand the data 
res = data.isnull().sum()
print(res)


#Handle Null Data 
ndata = data.fillna({ 
	"Glucose":data["Glucose"].mean(),
	"BloodPressure":data["BloodPressure"].mean(),
	"SkinThickness":data["SkinThickness"].mean(),
	"Insulin":data["Insulin"].mean(),
	"BMI":data["BMI"].mean()
})

# understand the data 
res = ndata.isnull().sum()
print(res)

#features ans target
features = ndata.drop("Outcome",axis ="columns")
target = ndata["Outcome"]
print(features)
print(target)

#features scalling 
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
nfeatures = mms.fit_transform(features)
print(nfeatures)

#find value of N 
N = int(len(ndata)**0.5)
if N % 2 == 0:
	N = N+1
print(N)

#train and Test the data 
x_train,x_test,y_train,y_test =train_test_split(nfeatures ,target)

#model and fit 
model =KNeighborsClassifier(n_neighbors = N,metric = "euclidean")
model.fit(x_train,y_train)

#plot_confusin matrix and classification_report
plot_confusion_matrix(model,x_test,y_test)
plt.show()

cr = classification_report(y_test,model.predict(x_test))
print(cr)

#predict
d= [[ 6 ,148.0,72.0,35.00000,155.548223, 33.6,0.627, 50]]
#d=[[]]
nd =mms.transform(d)
ans = model.predict(nd)
print(ans)

























