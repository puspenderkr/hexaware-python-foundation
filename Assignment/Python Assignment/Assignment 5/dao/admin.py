from util.database_connector import DBConnection

class Admin:
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_customer_to_database(self, customer):
        try:
            query = "INSERT INTO customers (customer_name, email, phone_number) VALUES (%s, %s, %s)"
            values = (customer.customer_name, customer.email, customer.phone_number)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Customer added to the database successfully.")
        except Exception as e:
            print(f"Error adding customer to the database: {e}")
            self.conn.rollback()

    def add_venue_to_database(self, venue):
        try:
            query = "INSERT INTO venues (venue_name, address) VALUES (%s, %s)"
            values = (venue.venue_name, venue.address)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Venue added to the database successfully.")
        except Exception as e:
            print(f"Error adding venue to the database: {e}")
            self.conn.rollback()