from db import db
import users
from sqlalchemy.sql import text

def get_list():
  sql = text("""SELECT C.content, U.username, Cat.name, C.sent_at, C.id 
             FROM chains C 
             JOIN users U ON C.user_id = U.id
             JOIN categories Cat ON C.category_id = Cat.id
             ORDER BY C.id""")
  result = db.session.execute(sql)
  return result.fetchall()

def send(content, category_id):
  user_id = users.user_id()
  if user_id == 0:
    return False
  sql = text("INSERT INTO chains (content, user_id, category_id, sent_at) VALUES (:content, :user_id, :category_id, NOW())")
  db.session.execute(sql, {"content":content, "user_id":user_id, "category_id":category_id})
  db.session.commit()
  return True