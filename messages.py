from db import db
import users
from sqlalchemy.sql import text

def get_messages(chain_id):
  sql = text("SELECT M.content, U.username FROM messages M, users U WHERE M.user_id=U.id AND M.chain_id=:chain_id order by M.id")
  result = db.session.execute(sql, {"chain_id":chain_id})
  return result.fetchall()

def send(content, chain_id):
  user_id = users.user_id()
  if user_id == 0:
    return False
  sql = text("INSERT INTO messages (content, chain_id, user_id) VALUES (:content, :chain_id, :user_id)")
  db.session.execute(sql, {"content":content, "chain_id":chain_id, "user_id":user_id})
  db.session.commit()
  return True