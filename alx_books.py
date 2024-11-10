import mysql.connector

# Establish the connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user= "Mukua# replace with your MySQL username
    password="J17-3640-2023"  # replace with your MySQL password
)

cursor = connection.cursor()

# Execute SQL script
with open("alx_book_store.sql", "r") as sql_file:
   sql_script = sql_file.read()
    
    # Split script by statements to execute one by one
    for statement in sql_script.split(';'):
        if statement.strip():
            try:
                cursor.execute(statement + ';')
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                print(f"Failed to execute: {statement}")

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
