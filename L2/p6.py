import pandas as pd
from sklearn.linear_model import LinearRegression 

data = pd.read_csv("abp.csv")
print(data)

features = data[["area","bedrooms"]]
target = data["price"]

model=LinearRegression()
model.fit(features,target)


b0 = model.intercept_
b1 = model.coef_[0]
b2 = model.coef_[1]
print(b0,b1,b2)

#area = float(input("Enter Area : "))
#bedrooms = float(input("Enter number of bedrooms : "))

#print("Price = ",price)