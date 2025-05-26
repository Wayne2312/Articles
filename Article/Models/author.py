import sqlite3

connection = sqlite3.connect("Articles.db")

class author:
    def __init__(self, name):
        self.name = name
        self.validate_name()
        
    def validate_name(self):
        if not self.name or len(self.name)<3:
            raise ValueError("Name must be at least 3 characters long.")

    def insert_author(self):
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO authors(name)
                VALUES(?)
            """, (self.name,))
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: the name: {self.name} is already in use")
    
    def search_author(self, value):
        cursor=connection.cursor()
        cursor.execute(
            """
            SELECT * FROM authors WHERE name = ?
            """
            ,(value,)
        )
        result=cursor.fetchall()
        return result
    
    def find_author_byid(self, author_id):
         cursor=connection.cursor()
         cursor.execute("""
                        SELECT * FROM authors WHERE id =?
                        """,(author_id))
         result=cursor.fetchone()
         return result