# train And testing data 
import pandas as pd
from sklearn.linear_model import LinearRegression 

data = pd.read_csv("abp.csv")
print(data)

features = data[["area","bedrooms"]]
target = data["price"]

model=LinearRegression()
model.fit(features,target)

#----------------------Prediction--------------------------------

area = float(input("Enter Area : "))
bedrooms = float(input("Enter number of bedrooms : "))

price = model.predict([[area,bedrooms]])

print("Price = ",price)