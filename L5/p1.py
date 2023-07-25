import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

#load data 

data = pd.read_csv("apple_sep2022.csv")
print(data)

#check null data 

res= data.isnull().sum()
print(res)

#imp1 = SimpleImputer(missing_values=np.nan , strategy="mean")
#mean ==> 3.5 + 5.0 + 6.5 +9.5 / 4 ======= 6.125

imp1 = SimpleImputer(missing_values=np.nan , strategy="constant",fill_value = 7.0)
#constant ==> 7.0

#imp1 = SimpleImputer(missing_values=np.nan , strategy="median")
#median ==> 3.5  5.0  6.5  9.5  ======= 5.75

data["price"]= imp1.fit_transform(data[["price"]])
print(data)

feature = data[["qty"]]
target = data["price"]


x_train,x_test,y_train,y_test= train_test_split(feature , target)
model = LinearRegression()
model.fit(x_train,y_train)



#score 

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)

print(s1)
print(s2)

#predict

qty = float(input("Enter Qty: "))
price = model.predict([[qty]])
print("Price = ",price)













