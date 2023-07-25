from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
	return "Home Page KC"

@app.route("/about")
def about():
	return "About Page of KC"

@app.route("/contact")
def contact():
	return "contact 8828478086"

if __name__ == "__main__":
	app.run(use_reloader = True)