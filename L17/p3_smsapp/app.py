from flask import Flask ,request,render_template
from sqlite3 import *

app =  Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
	con = None
	try:
		con = connect("kc.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		return render_template("home.html",msg=data)
	except Exception as e:
		msg = "issue "+ str(e)
		return render_template("home.html",msg=msg)
	finally :
		if con is not None:
			con.close()
	return render_template("home.html")


@app.route("/create",methods = ["GET","POST"])
def create():
	if request.method == "POST":
		rno = int(request.form["rn"])
		name = request.form["na"]
		con = None
		try :
			con = connect("kc.db")
			cursor = con.cursor()
			sql = "insert into student values('%d','%s')"
			cursor.execute(sql %(rno,name))
			con.commit()
			return render_template("create.html",msg="Record Created")
		
		except Exception as e:
			con.rollback()
			msg = "issue" +str(e)
			return render_template("create.html",msg=msg)
 			
		finally :
			if con is not None:
				con.close()
	else:
		return render_template("create.html")


if __name__ == "__main__":
		app.run(debug=True ,use_reloader=True)












	