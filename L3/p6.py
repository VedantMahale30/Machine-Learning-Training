import pandas as pd 

data = pd.read_csv("data.csv")
print(data)

r1 = data.isnull().sum()
print(r1)


#find whoose salary is null
r2 = data[data.Salary.isnull()]
print(r2)

#find whose exp is null
r3 = data[data.Experience.isnull()]
print(r3)

#find whoose age and position is null
r4 = data[(data.Age.isnull())& (data.Position.isnull())]
print(r4)


#find whose any column is null
r5 =data[data.isnull().any(axis =1)]
print(r5)



