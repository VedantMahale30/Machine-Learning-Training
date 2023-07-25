from flask import Flask,render_template,request
from math import pi ,pow
app=Flask(__name__)

@app.route("/",methods =["GET","POST"])
def home():
	if(request.method =="POST") and ("btna"in request.form):
		radius = float (request.form["rad"])
		area = pi* pow(radius,2)
		area = round(area,2)
		msg = "area = " +str(area)
		return render_template("home.html",msg=msg)

	elif(request.method =="POST") and ("btnc"in request.form):
		radius = float (request.form["rad"])
		circum = 2 *pi* radius
		circum = round(circum,2)
		msg = "circum = " +str(circum)
		return render_template("home.html",msg=msg)

	elif(request.method =="POST") and ("btnac"in request.form):
		radius = float (request.form["rad"])
		area = pi* pow(radius,2)
		area = round(area,2)
		circum = 2 * pi * radius
		circum = round(circum,2)
		msg =   "circum = " +str(circum)  +  "area = " +str(area)
		return render_template("home.html",msg=msg)
	
	
	else :
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)

