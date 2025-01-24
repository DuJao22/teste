from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

DATABASE = 'database/shopping_list.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def register_user(username, password):
    hashed_password = generate_password_hash(password)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    db.commit()
    db.close()

def login_user(username, password):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    db.close()
    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        return True
    return False

def logout_user():
    session.pop('user_id', None)

def is_logged_in():
    return 'user_id' in session

def get_current_user():
    if is_logged_in():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
        user = cursor.fetchone()
        db.close()
        return user
    return None