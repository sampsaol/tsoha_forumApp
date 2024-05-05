from db import db
import users
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError

def get_list():
  sql = text("SELECT name FROM categories ORDER BY name")
  result = db.session.execute(sql)
  return result.fetchall()

def add_category(category):
  user_id = users.user_id()
  if user_id == 0:
    return False
  try:
    sql = text("INSERT into categories (name) VALUES (:name)")
    db.session.execute(sql, {"name":category})
    db.session.commit()
    return True
  except IntegrityError:
    db.session.rollback()
    return False
  