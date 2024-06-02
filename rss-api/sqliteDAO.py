"""This module contains a concrete implementation of the abstract base class interfaces.dao.DataAccessObject using
SQLite3."""
import sqlite3
from interfaces.dao import DataAccessObject


class SQLiteDAO(DataAccessObject):
    """An implementation of the DataAcessObject using SQLite3.

    Attribute:
        filepath: The filepath to the database.
    """
    filepath: str

    def __init__(self, filepath: str):
        self.filepath = filepath

    def write_url(self, name: str, url: str) -> bool:
        database = sqlite3.connect(self.filepath)
        cursor = database.cursor()
        try:
            cursor.execute("INSERT INTO urls (url, name) VALUES (?, ?)", (url, name))
            status = True
        except sqlite3.Error as e:
            print(e.sqlite_errorcode, e.sqlite_errorname)
            status = False

        database.commit()
        database.close()
        return status

    def remove_url(self, name: str) -> bool:
        database = sqlite3.connect(self.filepath)
        cursor = database.cursor()
        try:
            cursor.execute("""DELETE FROM "urls" WHERE "name" = ?""", (name,))
            status = True
        except sqlite3.Error as e:
            print(e.sqlite_errorcode, e.sqlite_errorname)
            status = False

        database.commit()
        database.close()
        return status

    def get_urls(self) -> dict[str, str]:
        database = sqlite3.connect(self.filepath)
        cursor = database.cursor()
        urls = {}
        try:
            cursor.execute("""SELECT * FROM "urls";""")
            for row in cursor:
                urls[row[1]] = row[2]
        except sqlite3.Error as e:
            print(e)

        database.close()
        return urls
