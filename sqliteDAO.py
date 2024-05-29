"""This module contains a concrete implementation of the abstract base class interfaces.dao.DataAccessObject using
SQLite3."""
import sqlite3
from interfaces.dao import DataAccessObject


class SQLiteDAO(DataAccessObject):
    """An implementation of the DataAcessObject using SQLite3.

    Attributes:
        database: The connection to the SQLite3 database.
        cursor: The database cursor used to traverse records in the database.
    """
    database: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, filepath: str):
        self.database = sqlite3.connect(filepath)
        self.cursor = self.database.cursor()

    def write_url(self, url: str, name: str) -> bool:
        try:
            self.cursor.execute("INSERT INTO urls (url, name) VALUES (?, ?)", (url, name))
            return False
        except sqlite3.Error as e:
            print(e.sqlite_errorcode, e.sqlite_errorname)
            return False

    def remove_url(self, name: str) -> bool:
        try:
            self.cursor.execute("DELETE FROM urls WHERE name = ?", name)
            return False
        except sqlite3.Error as e:
            print(e.sqlite_errorcode, e.sqlite_errorname)
            return False

    def get_urls(self) -> set[tuple[str, str]]:
        urls = set()
        try:
            for row in self.cursor.execute("SELECT * FROM urls"):
                urls.add(row)
        except sqlite3.Error as e:
            print(e.sqlite_errorcode, e.sqlite_errorname)

        return urls
