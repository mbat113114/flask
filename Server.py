from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html", homeClass= "nav-link active", postClass ='nav-link', profileClass ='nav-link', aboutClass = 'nav-link')

@app.route("/about")
def about():
	return render_template("about.html", homeClass= "nav-link", postClass ='nav-link', profileClass ='nav-link', aboutClass = 'nav-link active')

@app.route("/profile")
def profile():
	return render_template("profile.html", homeClass= "nav-link", postClass ='nav-link', profileClass ='nav-link active', aboutClass = 'nav-link')

@app.route("/post")
def post():
	return render_template("post.html", homeClass= "nav-link", postClass ='nav-link active', profileClass ='nav-link', aboutClass = 'nav-link')


if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port = 8080)
