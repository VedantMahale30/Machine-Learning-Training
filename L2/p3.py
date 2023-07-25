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


b0 = model.intercept_
b1 = model.coef_
exp = float(input("Enter U r experience:"))
sal = b0 + b1* exp
print("Your salary Migth be ---> ",sal) 