import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("vehicle_data_sep2022.csv")
print(data)

plt.scatter(data["Age"],data["Vehicle"])
plt.xlabel("Age")
plt.ylabel("Vehicle")
plt.show()