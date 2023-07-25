import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("es.csv")

feature = data[["exp"]]
target =  data["sal"]

x_train,x_test,y_train,y_test = train_test_split(feature,target)

model = LinearRegression()
model.fit(x_train,y_train)

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)
print("Train Performance = ", s1*100)
print("Test Performance =",s2*100)

