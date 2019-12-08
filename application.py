from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')
@app.route("/", methods = ["GET"])
def index():
    return render_template("home.html")

@app.route("/home", methods = ["GET"])
def home():
    return render_template("home.html")

@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")

@app.route("/cart", methods = ["POST"])
def cart():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)