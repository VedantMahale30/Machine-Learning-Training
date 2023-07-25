import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("pets.csv")
print(data)

features = data[["exp","test"]]
target = data["salary"]

x_train,x_test,y_train,y_test = train_test_split(features , target)

model = LinearRegression()
model.fit(x_train,y_train)

s1 = model.score(x_train,y_train)
print("Score of train = ",s1)
s2 = model.score(x_test,y_test)
print("score of test =",s2)