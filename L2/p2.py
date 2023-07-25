import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("es.csv")
#print(data)

feature = data[["exp"]]
target = data["sal"]

#print(feature)
#print(target)

model = LinearRegression()
model.fit(feature,target)

exp = float(input("Enter Experience "))
sal = model.predict([[exp]])
print("Salary migth be = ",sal)