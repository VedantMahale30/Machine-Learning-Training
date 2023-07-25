from flask import Flask, render_template,request, url_for, redirect,session
from sqlite3 import *

app = Flask(__name__)
app.secrete_key = "Vedant is here"


@app.route("/",methods = ["GET","POST"])
def home():
	if "un" in session:
		if request.method=="POST":
			session.pop('un',None)
			return redirect( url_for('login'))
		else:
			return render_template("home.html",msg=session["un"])
	else:
		return redirect( url_for('login'))



@app.route("/signup",methods = ["GET","POST"])
def signup():
	if "un" in session:
		return redirect( url_for("home"))


	if request.method=="POST":
		un = request.form["un"]
		pw1 = request.form["pw1"]
		pw2 = request.form["pw2"]
		if pw1 == pw2 :
			con=None
			try:
				con = connect("kc.db")
				cursor = con.cursor()
				sql = "insert into users values('%s','%s')"
				cursor.execute(sql %(un,pw1))
				con.commit()
				return redirect(url_for('login'))
			except Exception as e:
				con.rollback()
				return render_template("signup.html",msg="User Already exists" +str(e))
			
			finally:
				if con is not None:
					con.close()
		
		else :
			return render_template("signup.html",msg="Password Did not match")


	else:
		return render_template("signup.html")






@app.route("/login",methods = ["GET","POST"])	
def login():
	if "un" in session:
		return redirect( url_for("home"))
		
	if request.method =="POST":
		un = request.form["un"]
		pw = request.form["pw"]
		con = None
		try :
			con = connect("kc.db")
			cursor = con.cursor()
			sql = "select * from users where username = '%s' and password = '%s'"
			
			cursor.execute(sql %(un,pw))
			data = cursor.fetchall()
			if len(data) == 0:
				return render_template("login.html",msg="Invalid Login")
			else:
				session['un'] = un	
				return redirect(url_for('home'))
		
		except Exception as e:
				return render_template("login.html",msg=str(e))
			
		finally:
				if con is not None:
					con.close()
	else:
		return render_template("login.html")


@app.errorhandler(404)
def not_found(e):
	return redirect( url_for('login'))


if __name__ =="__main__":
	app.run(debug =True,use_reloader=True)


	








