import pickle

f = None
model = None
try:
	f = open("diabetes.model","rb")
	model = pickle.load(f)

except Exception as e:
	print("f issue",e)

finally:
	if f is not None:
		f.close()

if model is not None:
	fs = float(input("Enter Fasting Sugar"))
	fu = input("frequent urination 1 for no  adn 2 for yes")
	if f ==1:
		data = [[fs,1,0]]
	else :
		data =[[fs,0,1]]
	
	ans =model.predict(data)
	print(ans[0])

else:
	print("model issue")