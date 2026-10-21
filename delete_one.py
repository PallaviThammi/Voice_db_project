import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# This line is SQL. Read it out loud:
# "DELETE FROM students WHERE name = 'Bob'"
cursor.execute("DELETE FROM students WHERE name = ?", ("Pallavi",))

print("Rows deleted:", cursor.rowcount)   # should be 1

conn.commit()   # <-- saves the change permanently

# Show what's left
rows = cursor.execute("SELECT * FROM students").fetchall()
print("Students remaining:")
for row in rows:
    print("  ", row)

conn.close()