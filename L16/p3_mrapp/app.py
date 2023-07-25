from flask import Flask,request,render_template
from sqlite3 import *

app = Flask("__name__")

@app.route("/",methods = ["GET","POST"])

def home():	
	if request.method=="POST":
		mn = request.form["mn"]
		rv = request.form["rv"]
		print(mn,rv)
		con = None
		try :
			con = connect("movie_review.db")
			cursor = con.cursor()
			sql = "insert into mr values('%s','%s')"
			cursor.execute(sql %(mn,rv))
			con.commit()
			msg = "Thanks for the review"
			return render_template("home.html",msg=msg)
		except Exceptioon as e :
			con.rollback()
			msg = "Issues "+str(e)
			return render_template("home.html",msg=msg)
		finally:
			if con is not None:
				con.close()
	else:	
		return render_template("home.html")	


if __name__=="__main__":
			
		app.run(debug=True,use_reloader=True)	









		