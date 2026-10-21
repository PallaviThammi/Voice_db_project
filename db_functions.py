import sqlite3

DB_NAME = "school.db"

def delete_student(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name = ? COLLATE NOCASE", (name,))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted

def list_students():
    conn = sqlite3.connect(DB_NAME)
    rows = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return rows