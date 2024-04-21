from app import app
from flask import render_template, request, redirect, session, abort
import chains, messages, users

@app.route("/")
def index():
  if users.user_id() == 0:
    return redirect("/login")
  else:
    chain_list = chains.get_list()
    user = users.get_username()
    return render_template("index.html", chains=chain_list, username=user)
  
@app.route("/chains")
def chain():
  if users.user_id() == 0:
    return redirect("/login")
  else:
    chain_list = chains.get_list()
    user = users.get_username()
    return render_template("index.html", chains=chain_list, username=user)
  
@app.route("/new-topic")
def new_topic():
  return render_template("new-topic.html")
  
@app.route("/send-topic", methods=["POST"])
def send_topic():
  content = request.form["content"]
  category = request.form["category"]
  if session["csrf_token"] != request.form["csrf_token"]:
    abort(403)
  if chains.send(content, category):
    return redirect("/")
  else:
    return render_template("error.html", message="Creating a topic failed")

@app.route("/chains/<int:id>")
def see_chain(id):
  messages_list = messages.get_messages(id)
  return render_template("see-messages.html", messages=messages_list, count=len(messages_list), chain_id=id)

@app.route("/new-message/<int:id>")
def new_message(id):
  return render_template("new-message.html", chain_id=id)

@app.route("/send-message", methods=["POST"])
def send_message():
  content = request.form["content"]
  chain_id = request.form["chain_id"]
  if session["csrf_token"] != request.form["csrf_token"]:
    abort(403)
  if messages.send(content, chain_id):
    url = "/chains/" + str(chain_id)
    return redirect(url)
  else:
    return render_template("error.html", message="Posting a message failed")

@app.route("/login", methods=["GET", "POST"])
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
  return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")
  if request.method == "POST":
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
      return render_template("error.html", message="Passwords do not match")
    if len(password1) < 8 or len(username) < 4:
      return render_template("error.html", message="Password or username too short")
    if users.register(username, password1):
      return redirect("/")
    else:
      return render_template("error.html", message="Registration unsuccesful, username must be unique")
  