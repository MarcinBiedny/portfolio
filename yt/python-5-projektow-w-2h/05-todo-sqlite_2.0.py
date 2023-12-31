import sqlite3

connection = sqlite3.connect("yt/python-5-projektow-w-2h/05-todo_2.0.db")


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


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task (task text)""")
    except:
        pass


def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()

    if len(result) == 0:
        print("You don't have any tasks yet!")
    else:
        print("Your tasks:")
        for row in result:
            print(str(row[0]) + " - " + row[1])


def add_task(connection):
    print("Add a task. Select '0' to return to the Menu.")
    task = input("Enter the content of the task: \n")
    if task == "0":
        print("Back to Menu.")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        connection.commit()
        print("Task added!")


def delete_task(connection):
    while True:
        task_index = input("Enter the index of the task to be deleted: \n")
        if not is_integer(task_index):
            print("It's not a number!")
            return False
        else:
            task_index = int(task_index)
            break

    cur = connection.cursor()
    rows_deleted = cur.execute(
        """DELETE FROM task WHERE rowid=?""", (task_index,)
    ).rowcount
    connection.commit()

    if rows_deleted == 0:
        print("Such a task does not exist!")
    else:
        print("Task deleted!")


create_table(connection)

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
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

connection.close()
