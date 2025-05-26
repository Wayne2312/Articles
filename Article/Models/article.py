import sqlite3

connection=sqlite3.connect("Articles.db")

class articles:
    def __init__(self, Title):
        self.Title=Title
        self.validate_Title()
        
    def validate_Title(self):
        if not self.Title or len(self.Title)<5:
            raise ValueError("Tiltle should be atleast 5 characters")
        
    def insert_article(self):
        try:
            cursor=connection.cursor()
            cursor.execute(
                """
                INSERT INTO articles(title)
                VALUES(?)
                """,(self.Title,)
            )
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: the Title: {self.Title} is already in use")
    
    def find_article_by_id(self, article_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM articles WHERE id = ?
        """, (article_id,))
        result = cursor.fetchone()
        return result

    def find_articles_by_title(self, title):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM articles WHERE title LIKE ?
        """, (f'%{title}%',))
        results = cursor.fetchall()
        return results

    def find_articles_by_author(self, author_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM articles WHERE author_id = ?
        """, (author_id,))
        results = cursor.fetchall()
        return results

    def find_articles_by_magazine(self, magazine_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM articles WHERE magazine_id = ?
        """, (magazine_id,))
        results = cursor.fetchall()
        return results