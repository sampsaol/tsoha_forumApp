from app import app
from flask import render_template, request, redirect, session, abort
import chains, messages, users, categories


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
  existing_categories = categories.get_list()
  return render_template("new-topic.html", existing_categories=existing_categories)
  
@app.route("/send-topic", methods=["POST"])
def send_topic():
  existing_categories = categories.get_list()
  content = request.form["content"]
  category = request.form["category"]
  category_id = categories.get_id(category)
  if session["csrf_token"] != request.form["csrf_token"]:
    abort(403)
  if len(content) > 1000:
    return render_template("new-topic.html", error="Topic too long (max 1000 characters)", content=content, category=category, existing_categories=existing_categories)
  if len(content) == 0:
    return render_template("new-topic.html", error="Topic must not be empty", content=content, category=category, existing_categories=existing_categories)
  if chains.send(content, category_id):
    return redirect("/")
  else:
    return render_template("new-topic.html", error="Creating a topic failed", content=content, category=category, existing_categories=existing_categories)

@app.route("/chains/<int:id>")
def see_chain(id):
  messages_list = messages.get_messages(id)
  username = users.get_username()
  return render_template("see-messages.html", messages=messages_list, count=len(messages_list), chain_id=id, username=username)

@app.route("/new-message/<int:id>")
def new_message(id):
  return render_template("new-message.html", chain_id=id)

@app.route("/send-message", methods=["POST"])
def send_message():
  content = request.form["content"]
  chain_id = request.form["chain_id"]
  if session["csrf_token"] != request.form["csrf_token"]:
    abort(403)
  if len(content) > 5000:
    return render_template("new-message.html", error="Message is too long (max 5000 characters)", content=content, chain_id=chain_id)
  if len(content) == 0:
    return render_template("new-message.html", error="Message must not be empty", content=content, chain_id=chain_id)
  if messages.send(content, chain_id):
    url = "/chains/" + str(chain_id)
    return redirect(url)
  else:
    return render_template("new-message.html", error="Posting a message failed", content=content, chain_id=chain_id)

@app.route("/like-message", methods=["POST"])
def like_message():
  message_id = request.form["message_id"]
  chain_id = request.form["chain_id"]
  if session["csrf_token"] != request.form["csrf_token"]:
    abort(403)
  url = "chains/" + str(chain_id)
  if messages.like(message_id):
    return redirect(url)
  else:
    return redirect(url)
  
@app.route("/new-category")
def new_category():
  existing_categories = categories.get_list()
  return render_template("new-category.html", existing_categories=existing_categories)
  
@app.route("/send-category", methods=["POST"])
def send_category():
  category = request.form["category"]
  existing_categories = categories.get_list()
  if session["csrf_token"] != request.form["csrf_token"]:
    abort(403)
  if len(category) > 100:
    return render_template("new-category.html", error="Category too long (max 100 characters)", category=category, existing_categories=existing_categories)
  if len(category) == 0:
    return render_template("new-category.html", error="Category must not be empty", category=category, existing_categories=existing_categories)
  if categories.add_category(category):
    return redirect("/")
  else:
    return render_template("new-category.html", error="Creating category failed. Note that category must be unique", category=category, existing_categories=existing_categories)

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
      return render_template("login.html", error="Wrong username or password", username=username)
    
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
      return render_template("register.html", error="Passwords do not match", username=username)
    if len(password1) < 8 or len(username) < 4:
      return render_template("register.html", error="Password or username too short (password min 8 characters, username min 4 characters)", username=username)
    if users.register(username, password1):
      return redirect("/")
    else:
      return render_template("register.html", error="Registration unsuccesful, username must be unique", username=username)
  