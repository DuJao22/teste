from flask import session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
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

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
Você pode copiar e colar este código no seu arquivo utils/auth.py.

Valeu demais 
De nada! Se precisar de mais alguma coisa, é só falar. Boa sorte com o deploy!

Code
Issues
Pull requests
teste/utils
/auth.py
DuJao22
DuJao22
3 hours ago
45 lines (38 loc) · 1.22 KB

Code

Blame
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
    
