import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='Mukua',  # replace with your MySQL username
            password='J17-3640-2023'  # replace with your MySQL password
        )

        # Check if the connection is established
        if connection.is_connected():
            print("Successfully connected to MySQL server")

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # SQL statement to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Commit the transaction (for creating database)
            connection.commit()

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Catch any MySQL specific errors and print the error
        print(f"Error: {err}")

    finally:
        # Ensure that the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
