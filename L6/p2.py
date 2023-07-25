from sklearn.datasets import load_boston
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

bd = load_boston()
print(bd)
data = pd.DataFrame(bd.data,columns = bd.feature_names)
data["Price"] = bd.target
print(data)

res = data.isnull().sum()
print(res)

#find Feature importance 
corr_matrix = data.corr()
corr_matrix.to_csv("cm.csv")
print(corr_matrix)

features = data[["RM","LSTAT"]]
target = data["Price"]
print(features.head())
print(target.head())

x_train, x_test, y_train, y_test = train_test_split(features ,target)

model = LinearRegression()
model.fit(x_train,y_train)

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)
print(s1)
print(s2)

data = [[6.998 , 2.94]]
data = [[7.185  ,4.03]]
price = model.predict(data)
print("Price = ", price)









