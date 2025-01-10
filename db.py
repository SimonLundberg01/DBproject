import mysql.connector

# Global variables for connection and cursor
connection = None
cursor = None

def initialize_connection():
    """Initialize the database connection and cursor."""
    global connection, cursor
    if connection is None or not connection.is_connected():
        connection = mysql.connector.connect(
            host='127.0.0.1',  # Replace with your MySQL host
            user='root',       # Replace with your MySQL username
            password='Salle123!',  # Replace with your MySQL password
            database='recipes'     # Replace with your database name
        )
        cursor = connection.cursor()

def close_connection():
    """Close the database connection and cursor."""
    global connection, cursor
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")
