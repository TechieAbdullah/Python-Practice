import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

print(mydb)

def create_city_table():
    if mydb.is_connected():
        cursor = mydb.cursor()
        create_city_table_query = """
            CREATE TABLE city (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city_name VARCHAR(100) NOT NULL
            )
        """
        cursor.execute(create_city_table_query)
        print("Table 'city' created successfully.")
        
        insert_city_data_query = """
            INSERT INTO city (city_name)
            VALUES (%s)
        """
        city_data = [
            ('Lahore',),
            ('FSD',),
            ('Karachi',)
        ]
        cursor.executemany(insert_city_data_query, city_data)
        mydb.commit()
        print("Sample data inserted into 'city' successfully.")
        cursor.close()

def create_student_table_and_insert_data():
    if mydb.is_connected():
        cursor = mydb.cursor()
        create_student_table_query = """
            CREATE TABLE student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                cityid INT,
                city VARCHAR(100),
                FOREIGN KEY (cityid) REFERENCES city(id)
            )
        """
        cursor.execute(create_student_table_query)
        print("Table 'student' created successfully.")
        
        insert_student_data_query = """
            INSERT INTO student (name, cityid, city)
            VALUES (%s, %s, %s)
        """
        student_data = [
            ('Ali', 1, 'Lahore'),
            ('Ubaid', 2, 'FSD'),
            ('Abdullah', 3, 'Karachi'),
            ('Hamza', 1, 'Lahore')
        ]
        cursor.executemany(insert_student_data_query, student_data)
        mydb.commit()
        print("Sample data inserted into 'student' successfully.")
        cursor.close()
        mydb.close()
        print("MySQL connection is closed.")

create_city_table()
create_student_table_and_insert_data()