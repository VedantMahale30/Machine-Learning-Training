from flask import Flask,request,render_template
from sqlite3 import *

app = Flask(__name__)
@app.route("/",methods =["GET","POST"])

def home():
	if request.method == "POST":
		name = request.form["na"]
		choice = request.form["c"]
		print(name , choice)
		con = None
		try:
			con =connect("wn.db")
			cursor = con.cursor()
			sql = "insert into student values('%s','%s')"
			cursor.execute(sql %(name,choice))
			con.commit()
			return render_template("home.html",msg="Thank You")
		except Exception as e:
			con.rollback()
			return render_template("home.html",msg="Inssue" +e)
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("home.html")
	
if __name__=="__main__":
	app.run(debug=True,use_reloader=True)
			










