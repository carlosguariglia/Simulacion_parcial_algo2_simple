import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute(self, query, params=()):
        """Execute a query with the given parameters."""
        try:
            cursor = self.connection.cursor()
            result = cursor.execute(query, params)
            self.connection.commit()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            return None

    def fetchall(self, query, params=()):
        """Fetch all results of a query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")
            return []

    def fetchone(self, query, params=()):
        """Fetch a single result of a query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"The error '{e}' occurred")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection to SQLite DB closed")