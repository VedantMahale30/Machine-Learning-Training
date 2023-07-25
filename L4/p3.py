# n- 1 stratergy 
import pandas as pd 
from sklearn.linear_model import LinearRegression 

data = pd.read_csv("papsep2022.csv")
print(data)

print("***************************************************************************")

dummies  = pd.get_dummies (data.place, drop_first=True)
print(dummies)

print("***************************************************************************")

ndata =  pd.concat([data,dummies],axis ="columns")
print(ndata)

features = ndata[["area","Khandala","Lonavala"]]
target = ndata["price"]

model= LinearRegression()
model.fit(features, target)


area = int(input("Enter Area : "))
location =int(input("1- Karjat ,2- Khandala , 3- Lonavala "))
if location == 1:
	data = [[area ,0,0]]
elif location==2:
	data = [[area ,1,0]]
else :
	data = [[area ,0,1]]

price =  model.predict(data)
print ("Price = ",price)








