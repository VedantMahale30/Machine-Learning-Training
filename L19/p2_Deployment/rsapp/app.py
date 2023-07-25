from flask import Flask ,render_template ,request
import pickle

app = Flask(__name__)
@app.route("/",methods =["GET","POST"])

def home():
	if request.method  == "POST":
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

			area = float(request.form["area"])
			bedrooms = float(request.form["bedrooms"])
			data = [[area , bedrooms]]
			ans = model.predict(data)
			msg = "price = "+ str(round(ans[0],2)) + "crs"
			return render_template("home.html",msg=msg)
	
		else:
			print("model issue ")
	else:
		return render_template("home.html")

		
if __name__  == "__main__":
	app.run(debug=True,use_reloader=True)