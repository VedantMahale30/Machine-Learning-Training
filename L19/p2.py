import pickle
f = None
try:
	f = open("re.model","rb")
	model = pickle.load(f)
	
except Exception as e:
	print("issue ",e)

finally:
	if f is not None:
		f.close()
	
if model is not None:
	area = float(input("Enter Area : "))
	bedrooms = float(input("Enter Bedrooms :"))
	data = [[area , bedrooms]]
	ans = model.predict(data)
	print("price = ",round(ans[0],2),"crs")

else:
	print("model issue ")


