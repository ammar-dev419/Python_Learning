from database import *
db = Database()
from task import *

def add_task():
    title = input("Enter task title: ")
    description = input("Enter description: ")
    user_id = int(input("Enter user id: "))
    db.cursor.execute("""
                   INSERT INTO tasks (title, description, done, user_id) 
                   VALUES (?, ?, ?, ?)""", 
                   (title, description, 0, user_id))
    db.connection.commit()
    print("Task added successfully.")

def show_task():
    db.cursor.execute("SELECT * FROM tasks")
    rows = db.cursor.fetchall()
    tasks = []
    for row in rows:
        task = Task(row[1], row[2], row[3], row[4])
        tasks.append(task)
    for task in tasks:
        print("=====================")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Done: {task.done}")
        print(f"User_ID: {task.user_id}")

def complete_task():
    task_id = int(input("Enter task id: "))
    db.cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (1, task_id))
    db.connection.commit()
    print("Task completed.")

def delete_task():
    task_id = int(input("Enter task id: "))
    db.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.connection.commit()
    print("Task delete.")

def search_task():
    task_id = int(input("Enter task id: "))
    db.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = db.cursor.fetchone()
    print("=====================")
    print(f"ID: {task[0]}")
    print(f"Title: {task[1]}")
    print(f"Description: {task[2]}")
    print(f"Done: {task[3]}")

def sort_tasks():
    db.cursor.execute("SELECT * FROM tasks ORDER BY id ASC")
    tasks = db.cursor.fetchall()
    for task in tasks:
        print("=====================")
        print(f"ID: {task[0]}")
        print(f"Title: {task[1]}")
        print(f"Description: {task[2]}")
        print(f"Done: {task[3]}")

def search_by_title():
    keyword = input("Rechercher : ")
    db.cursor.execute("SELECT * FROM tasks WHERE title LIKE ?", (f"%{keyword}%",))
    tasks = db.cursor.fetchall()
    for task in tasks:
        print("=====================")
        print(f"ID: {task[0]}")
        print(f"Title: {task[1]}")
        print(f"Description: {task[2]}")
        print(f"Done: {task[3]}")

def show_tasks_with_users():
    db.cursor.execute("""
SELECT users.name, tasks.title
                   FROM users
                   JOIN tasks
                   ON users.id = tasks.user_id
                   """)
    tasks = db.cursor.fetchall()
    for task in tasks:
        print("=====================")
        print(f"User: {task[0]}")
        print(f"Task: {task[1]}")
        print("=====================")
