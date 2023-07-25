from flask import Flask,render_template,request
from random import *
from flask_mail import Mail,Message

app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] ="tester.aditya28sept22@gmail.com"
app.config["MAIL_PASSWORD"] ="sylxrcaxevovpxdl"
app.config["MAIL_TLS"] = True
app.config["MAIL_SSL"] = False


mail =Mail(app)
	
@app.route("/",methods = ["GET","POST"])
def home():
	if request.method == "POST":
		em = request.form["em"]
		length = int( request.form["length"])
		uc = "uc" in request.form
		di = "di" in request.form
		text = "abcdefghijklmnopqrstwxyz"

		if uc:
			text = text + text.upper()
		if di:
			text = text+"0123456789"
		
		pw = ""
		for i in range(length):
			r  = randrange(len(text))
			pw = pw +text[r]
		msg = "password is +str(pw)"
	
	
		subject = "Password from PG app"
		sender = "tester.aditya28sept22@gmail.com"	
		recipient = [em]
		message = Message(subject, sender=sender , recipients = recipients)
		message.body =msg
		mail.send(message)
		return render_template("home.html",msg=msg)

	else:

		return render_template("home.html")


if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)






