from classes.sqlite import  SQLite
from classes.task import  Task
from pathlib import Path

DEFAULT_DB_NAME = "todo.db"

def is_integer(value):
    try:
        int(value)
    except Exception:
        return False
    return True

def is_user_choice_within_proper_range(user_choice):
    if 1 <= int(user_choice) <= 4:
        return True
    return False

def is_valid_user_choice_within_proper_range(user_choice):
    if not is_integer(user_choice):
        print("It's not a number!")
        return False
    if not is_user_choice_within_proper_range(user_choice):
        print("There is not such option in the Menu!")
        return False
    return True

if __name__ == '__main__':
    db = SQLite(str(Path( __file__ ).parent.absolute()) + "/" + DEFAULT_DB_NAME)

    try:
        db.create_table("task", ["task", "text"])
    except Exception as e:
        print ("Sorry error ocurred :(")

    task = Task(db)

    while True:
        print()
        print("MENU")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        user_choice = input("Choose a number: ")
        if is_valid_user_choice_within_proper_range(user_choice):
            user_choice = int(user_choice)
            print()

        if user_choice == 1:
            task.show_tasks(task)

        if user_choice == 2:
            task.add(task)

        if user_choice == 3:
            task.delete_task(task)

        if user_choice == 4:
            break

    #close()
