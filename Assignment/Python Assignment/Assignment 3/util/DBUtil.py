import mysql.connector

class DBUtil:
    @staticmethod
    def getDBConn():
        try:

            db_config = {
                'host': 'localhost',
                'user': 'root',
                'password': 'Aniket@123',
                'database': 'hmbank',
                'port': '3306',
            }

            connection = mysql.connector.connect(**db_config)

            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except Exception as e:
            print(f"Error: {e}")
            return None


