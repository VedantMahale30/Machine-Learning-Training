import pandas as pd 
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("abp.csv")
print(data)

res = data.isnull().sum()
print(res)

features = data[["area","bedrooms"]] 
target = data["price"]

model = LinearRegression()
model.fit(features,target)

f = None
try:
	f = open("re.model","wb")
	pickle.dump(model,f)

except Exception as e:
	print("issues",e)


finally:
	if f is not None:
		f.close()
	
	













