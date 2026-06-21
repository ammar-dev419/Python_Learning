from task_manager import *
from user_manager import *


while True:
    print("\n")
    print("=====================")
    print("1. Add task")
    print("2. Show task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Search task by id")
    print("6. Sort task")
    print("7. Search tasks by title")
    print("8. Add users")
    print("9. Show users")
    print("10. Show tasks with users")
    print("11. Exit")
    print("=====================")
    print("\n")
    command_list = str(input("Choisissez votre commande: "))
    print("\n")

    if command_list == "1":
        add_task()

    elif command_list == "2":
        show_task()

    elif command_list == "3":
        complete_task()

    elif command_list == "4":
        delete_task()

    elif command_list == "5":
        search_task()

    elif command_list == "6":
        sort_tasks()

    elif command_list == "7":
        search_by_title()

    elif command_list == "8":
        add_users()

    elif command_list == "9":
        show_users()

    elif command_list == "10":
        show_tasks_with_users()

    elif command_list == "11":
        break

    else:
        print("Commande invalide.")
        
db.connection.close()
