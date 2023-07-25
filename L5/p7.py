import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

data = pd.read_csv("pos_sal_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

feature = data[["Level"]]
target = data["Salary"]

pf = PolynomialFeatures(degree=4)
pfeature =pf.fit_transform(feature)

model= LinearRegression()
model.fit(pfeature , target)

plt.scatter(data["Level"],data["Salary"])
plt.plot(data["Level"],model.predict(feature))
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("TCS")
plt.show()
