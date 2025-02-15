import sqlite3

class Database:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def insert(self, name, age, course):
        self.cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def search(self, name):
        self.cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
        return self.cursor.fetchall()

    def delete(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()

    def update(self, student_id, name, age, course):
        self.cursor.execute("UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?", (name, age, course, student_id))
        self.conn.commit()

    def close(self):
        self.conn.close()
