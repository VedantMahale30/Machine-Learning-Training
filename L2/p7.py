import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("abp.csv")

features = data[["area","bedrooms"]]
target = data["price"]

x_train,x_test,y_train,y_test = train_test_split(features ,target,random_state=11 )

model= LinearRegression()
model.fit(x_train,y_train)

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)

print(s1 , s2)


area = float(input("Enter Area : "))
bedrooms = float(input("Enter number of bedrooms : "))

price = model.predict([[area,bedrooms]])

print("Price = ",price)