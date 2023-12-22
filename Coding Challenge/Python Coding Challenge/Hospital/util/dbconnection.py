import mysql.connector
from mysql.connector import Error

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                DBConnection.connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='hospital'
                )
                if DBConnection.connection.is_connected():
                    print("Connected to MySQL database")
            except Error as e:
                print(f"Error connecting to MySQL database: {e}")

        return DBConnection.connection
