from flask import Flask,render_template,request
from datetime import *

app = Flask(__name__)

@app.route("/")
def home():
	if request.args.get("na"):
		name = request.args.get("na")
		d = datetime.now()
		hr = d.hour
		rep = ""
		if hr<12:
			rep  = "Good Morning"
		elif hr < 16:
			rep = "Good Afternoon"
		else :
			rep = "Good Evening"

		msg = "Welcome " +name+ "" +rep
		return render_template("home.html",m=msg)

	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)