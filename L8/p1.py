#scatter Plot 

import pandas as pd 
import matplotlib.pyplot as plt

data =  pd.read_csv("age_movie_sep2022.csv")
print(data)

res = data.isnull().sum()
print(res)

plt.scatter(data["age"],data["movie"])
plt.xlabel("age")
plt.ylabel("movie")
plt.show()