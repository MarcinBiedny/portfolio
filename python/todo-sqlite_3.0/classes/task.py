class Task:

    _sqlite = None

    def __init__(self, sqlite) -> None:
        self._sqlite = sqlite

    def add(self, task):
        print("Add a task. Select '0' to return to the Menu.")
        task = input("Enter the content of the task: \n")
        cursor = self._sqlite.get_cursor()
        cursor.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        self._sqlite.connection_commit()


    def show_tasks(self, task):
        cursor = self._sqlite.get_cursor()
        cursor.execute("""SELECT rowid, task FROM task""")
        result = cursor.fetchall()

        if len(result) == 0:
            print("You don't have any tasks yet!")
        else:
            print("Your tasks:")
            for row in result:
                print(str(row[0]) + " - " + row[1])

    def delete_task(self, task):
        while True:
            task_index = input("Enter the index of the task to be deleted: \n")
            if not is_integer(task_index):
                print("It's not a number!")
                return False
            else:
                task_index = int(task_index)
                break
        
        cursor = self._sqlite.get_cursor()
        rows_deleted = cursor.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
        self._sqlite.connection_commit()

        if rows_deleted == 0:
            print("Such a task does not exist!")
        else:
            print("Task deleted!")

def is_integer(value):
    try:
        int(value)
    except Exception:
        return False
    return True
