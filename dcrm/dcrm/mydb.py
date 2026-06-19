import mysql.connector as conn

db = conn.connect(
    host = 'localhost',
    user = 'root',
    passwd = "Saahil@2005"
)

cursorObj = db.cursor()

try:
    cursorObj.execute("CREATE DATABASE IF NOT EXISTS elderco")
    print("Database created successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    db.close()

print("All Done!")