from flask import Flask ,request,render_template
from sqlite3 import *

app = Flask(__name__)

@app.route("/" ,methods=["GET","POST"])
def home():
		if request.method == "POST":
			name = request.form["na"]
			passport = request.form.get("passport")
			visa = request.form.get("visa")
			admit = request.form.get("admit")
			money = request.form.get("money")
			ttc = "";
			if passport :
				ttc +=" Passport"
			if visa :
				ttc +=" Visa"
			if admit :
				ttc +=" Admit"
			if money :
				ttc +=" Money"
			con = None
			try :
				con = connect("ttc.db")
				cursor = con.cursor()
				sql = "insert into student values('%s','%s')"	
				cursor.execute(sql %(name,ttc))
				con.commit()
				return render_template("home.html",msg="noted")
			except Exception as e:
				con.rollback()
				return render_template("home.html",msg="issue" +e)
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("home.html")


if __name__== "__main__":
	app.run(debug=True, use_reloader=True)	









				
				




