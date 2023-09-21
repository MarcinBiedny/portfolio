import sqlite3
from sqlite3 import Cursor


class SQLite:
    _connection = None

    def __init__(self, db_path: str) -> None:
        self._connection = sqlite3.connect(db_path)

    def create_table(self, table_name: str, columns: [str]):
        cursor = self._connection.cursor()

        query = """CREATE TABLE %s (%s)""" % (table_name, " ".join(columns))
        try:
            cursor.execute(query)
        except sqlite3.OperationalError:
            pass
        except Exception as e:
            raise Exception(e)

    def get_cursor(self) -> Cursor:
        return self._connection.cursor()

    def connection_commit(self):
        self._connection.commit()
        