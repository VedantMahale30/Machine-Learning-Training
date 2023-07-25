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


features = data.drop(["Price"], axis ="columns")
target = data["Price"]
print(features)
print(target)


x_train, x_test, y_train, y_test = train_test_split(features ,target)
model = LinearRegression()
model.fit(x_train,y_train)

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)
print(s1)
print(s2)


data =[[0.00632,18.0 , 2.31, 0.0,0.538, 6.575, 65.2, 4.0900, 1.0,  296.0, 15.3,396.90,4.98]]
data =[[0.06076, 0.0 ,11.93, 0.0,0.573,  6.976,  91.0, 2.1675,  1.0, 273.0, 21.0,396.90,5.64]]
price = model.predict(data)
print("Price = ", price)









