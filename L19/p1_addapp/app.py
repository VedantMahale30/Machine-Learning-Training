from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def home():
	if request.args.get("n1") and request.args.get("n2"):
		n1 = float(request.args.get("n1"))
		n2 = float(request.args.get("n2"))
		res = n1 + n2
		res = round(res,2)
		msg = "addn = "+ str(res)
		return render_template("home.html",msg=msg)
	else :
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)

