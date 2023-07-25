import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hp.csv")
print(data)

x = data["area"].tolist()
y = data["price"].tolist()
print(x)
print(y)

plt.scatter(x,y,color="red")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Lonavala Bunglow Price Prediction ")
plt.show()

