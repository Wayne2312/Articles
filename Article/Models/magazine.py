import sqlite3
from article import articles
from author import author

# Establish database connection
connection = sqlite3.connect("Articles.db")

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.validate_properties()

    def validate_properties(self):
        if not self.name or len(self.name) < 3:
            raise ValueError("Magazine name must be at least 3 characters long.")
        if not self.category or len(self.category) < 3:
            raise ValueError("Category must be at least 3 characters long.")

    def insert_magazine(self):
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO magazines(name, category) VALUES(?, ?)", (self.name, self.category))
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: the magazine '{self.name}' already exists.")

    def find_magazine_by_id(self, magazine_id):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        return cursor.fetchone()

    def find_magazine_by_name(self, name):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        return cursor.fetchall()

    def find_magazine_by_category(self, category):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        return cursor.fetchall()