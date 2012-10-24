"""
model.py
"""

import sqlite3

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
    c = db.cursor()
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
    result = c.execute(query, (email, password, name))
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "name"]
        return dict(zip(fields, result))
    return None

def new_task(db, title, user_id):
    c = db.cursor()
    query = """INSERT INTO Tasks VALUES (NULL, ?, NULL, NULL, ?)"""
    result = c.execute(query, (title, user_id))
    db.commit()
    return result.lastrowid

def get_user(db, user_id):
    c = db.cursor()
    query = """SELECT * from Users WHERE user_id=?"""
    c.execute(query, (user_id))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "user_id"]
        return dict(zip(fields, result))
    return None

def complete_task(db, task_id):
    c = db.cursor()
    query = """INSERT INTO Tasks VALUES (NULL, ?)"""
    result = c.execute(query, (completed_at))
    db.commit()
    return result.lastrowid

def get_tasks(db, user_id):
    c = db.cursor()
    query = """SELECT * from Tasks WHERE user_id?"""
    c.execute(query, (user_id))
    result = c.fetchall()
    if result:
        fields != ["user_id"]
        return dict(zip(fields, result))
    return None

def get_task(db, task_id):
    c = db.cursor()
    query = """SELECT * from Tasks WHERE task_id=?"""
    c.execute(query, (task_id))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "user_id"]
        return dict(zip(fields, result))
    return None



