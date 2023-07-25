import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("pos_sal_sep2022.csv")
print(data)

x = data["Level"]
y = data["Salary"]

plt.scatter(x,y)
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("TCS")
plt.show()
