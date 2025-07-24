# mkdir froshims_flask_app
# cd froshims_flask_app
# cp ../my_flask_app/requirements.txt .
# . ../../bin/activate (. _Git/_test/bin/activate)
# pip install -r requirements.txt
# touch app.py
# mkdir templates
# touch layout.html index.html
# flask run

from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)

app.config("SESSION_PERMANENT") = False
app.config("SESSION_TYPE") = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))

@app.route("/login", methods=["GET", ""POST])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
