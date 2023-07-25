import pandas as pd

data = pd.read_csv("data.csv")


d1 = data.fillna({"Salary":8000})
print(d1)

d2 = data.fillna({"Salary":data["Salary"].mean()})
print(d2)

d3 = data.fillna({"Age":20})
print(d3)

d4 = data.fillna({"Position":"Unallocated"})
print(d4)

d5 = data.fillna({"Experience":data["Experience"].mean()})
print(d5)