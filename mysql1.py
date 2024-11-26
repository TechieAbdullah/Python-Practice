import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",  
  database="pythondb"
)

print(mydb)
cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE pythondb")
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Ali", "Highway21")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()
for row in result:
    print(row)
cursor.close()
mydb.close()
print("MySQL connection is closed.")