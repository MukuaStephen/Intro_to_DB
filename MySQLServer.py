import mysql.connector
from mysql.connector import Error

# Function to create the database
def create_database():
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # MySQL server address
            user="Mukua",  # Replace with your MySQL username
            password="J17-3640-2023"  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Successfully connected to MySQL server")

            # Create a cursor object
            cursor = connection.cursor()

            # Create the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Commit the changes
            connection.commit()

            print("Database 'alx_book_store' created successfully!")
        
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function to create the database
if __name__ == "__main__":
    create_database()
