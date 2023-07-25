import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv( "result_data_sep2022.csv")
print(data)

plt.scatter(data["hr"],data["result"])
plt.xlabel("Hours")
plt.ylabel("Result")
plt.show()