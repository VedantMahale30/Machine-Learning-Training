import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("es.csv")
print(data)


x = data["exp"]
y = data["sal"]

plt.scatter(x,y)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("TCA - USA")

plt.show()