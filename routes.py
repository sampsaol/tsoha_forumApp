from app import app
from flask import render_template, request, redirect
import users

@app.route("/")
def index():
  if users.user_id() == 0:
    return redirect("/login")
  else:
    return render_template("index.html")
  
@app.route("/login")
def login():
  if request.method == "GET":
    return render_template("login.html")
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
      return redirect("/")
    else:
      return render_template("error.html", message="Wrong username or password")
    
@app.route("/logout")
def logout():
  users.logout()
  redirect("/")

@app.route("/register")
def register():
  if request.method == "GET":
    return render_template("register.html")
  if request.method == "POST":
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
      return render_template("error.html", message="Passwords do not match")
    if users.register(username, password1):
      return redirect("/")
    else:
      return render_template("error.html", message="Registration unsuccesful, username must be unique")
  