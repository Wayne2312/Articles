import sqlite3

connection=sqlite3.connect("Articles.db")
connection.row_factory=sqlite3.Row
cursor=connection.cursor()

#TABLE CREATION
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS authors(
      id INTEGER PRIMARY KEY,
      name VARCHAR(255) NOT NULL  
    )
    """
    )
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS magazines(
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        category VARCHAR(255) NOT NULL
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);

    """
)
cursor.execute("CREATE INDEX IF NOT EXISTS idx_authors_name ON authors(name)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_magazines_name ON magazines(name)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_title ON articles(title)")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_author_id ON articles(author_id)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_magazine_id ON articles(magazine_id)")
connection.commit()

