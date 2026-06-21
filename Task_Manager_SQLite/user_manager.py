from database import *
db = Database()
from user import *

def add_users():
    name = input("Enter user name: ")
    db.cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    db.connection.commit()
    print("The user was add successfully.")

def show_users():
    db.cursor.execute("SELECT * FROM users")
    rows = db.cursor.fetchall()
    users = []
    for row in rows:
        user = User(row[1])
        users.append(user)
    for user in users:
        print(user.name)