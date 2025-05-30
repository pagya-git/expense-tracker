import sqlite3

conn = sqlite3.connect('expense.db')
c = conn.cursor()

try:
    c.execute("ALTER TABLE expenses ADD COLUMN image TEXT;")
    print("Column 'image' added successfully.")
except sqlite3.OperationalError as e:
    print("Error:", e)

conn.commit()
conn.close()
