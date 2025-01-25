from flask import session, redirect, url_for, flash
from utils.auth import get_db

def get_all_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, username FROM users")
    return cursor.fetchall()

def get_user_shopping_list(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, item_name, is_purchased FROM shopping_list WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    cursor.execute("DELETE FROM shopping_list WHERE user_id = ?", (user_id,))
    db.commit()

def edit_user(user_id, new_username):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user_id))
    db.commit()

def mark_item_as_purchased(item_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE shopping_list SET is_purchased = 1 WHERE id = ?", (item_id,))
    db.commit()
