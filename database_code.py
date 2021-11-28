import sqlite3

connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()

command = """Create table if not exists users(name TEXT, Password TEXT)"""

cursor.execute(command)
cursor.execute("Insert into users values('Samridh', '1234')")

connection.commit()
cursor.close()