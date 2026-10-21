import sqlite3
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id   INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("DELETE FROM students")

students = [("Shiva",), ("Pallavi",), ("Ram",), ("Gita",)]
cursor.executemany("INSERT INTO students (name) VALUES (?)", students)

conn.commit()

rows = cursor.execute("SELECT * FROM students").fetchall()
print("Current students in the database:")
for row in rows:
    print("  ", row)

conn.close()
print("\nDatabase 'school.db' is ready.")