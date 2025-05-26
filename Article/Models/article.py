import sqlite3

connection = sqlite3.connect("Articles.db")

class article:
    def __init__(self, name):
        self.name = name

    def insert_author(self, value):
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO users(name)
                VALUES(?)
            """, (value,))
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: the name: {value} is already in use")