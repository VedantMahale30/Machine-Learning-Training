import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("temp_pressure_sep2022.csv")
print(data)

plt.scatter(data["temp"],data["pressure"])
plt.xlabel("Temp")
plt.ylabel("Pressure")
plt.show()
