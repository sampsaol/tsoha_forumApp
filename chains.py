from db import db
import users
from sqlalchemy.sql import text

def get_list():
  sql = text("SELECT C.content, U.username, C.category, C.sent_at, C.id FROM chains C, users U WHERE C.user_id=U.id ORDER BY C.id")
  result = db.session.execute(sql)
  return result.fetchall()

def send(content, category):
  user_id = users.user_id()
  if user_id == 0:
    return False
  sql = text("INSERT INTO chains (content, user_id, category, sent_at) VALUES (:content, :user_id, :category, NOW())")
  db.session.execute(sql, {"content":content, "user_id":user_id, "category":category})
  db.session.commit()
  return True