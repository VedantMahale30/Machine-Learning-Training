import pandas as pd 
from sklearn.tree import DecisionTreeRegressor,plot_tree
import matplotlib.pyplot as plt

data = pd.read_csv("salary_data.csv")
print(data)

feature = data[["Level"]]
target = data["Salary"]

model= DecisionTreeRegressor()
mf = model.fit(feature ,target)

level = float(input("Enter Level : "))
ans = model.predict([[level]])
print(ans)

plt.figure(figsize=(10,5))
plot_tree(mf,fontsize =10)
plt.show()




