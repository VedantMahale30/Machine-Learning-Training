import pandas as pd

print("---------------------------------------------------------------")
data = pd.read_csv("data.csv")
print(data)

print("---------------------------------------------------------------")
d1 = data.dropna(how="any")
print(d1)

print("---------------------------------------------------------------")
d2 =data.dropna(how="all")
print(d2)

print("---------------------------------------------------------------")
d3 =data.dropna(subset=["Salary"])
print(d3)

print("---------------------------------------------------------------")

# WHOOSE AGE AND POSITION IS NULL

d4 = data.dropna(subset=["Age","Position"],how="all")
print(d4)