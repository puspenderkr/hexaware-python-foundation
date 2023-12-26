from entity.customers import Customers
from exceptions.exception import DuplicateCustomerException, CustomerNotFoundException
from util.database_connector import DBConnection

class CustomerManager:
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_customer(self, customer):
        try:
            # Check if the customer with the same CustomerID or Email already exists
            self.cursor.execute("SELECT * FROM customers WHERE CustomerID = %s OR Email = %s",
                                (customer.get_customer_id(), customer.get_email()))
            existing_customer = self.cursor.fetchone()
            if existing_customer:
                raise DuplicateCustomerException("Customer with the same ID or Email already exists.")

            # Insert the new customer into the database
            self.cursor.execute("INSERT INTO customers (CustomerID, FirstName, LastName, Email, Phone, Address) "
                                "VALUES (%s, %s, %s, %s, %s, %s)",
                                (customer.get_customer_id(), customer.get_first_name(),
                                 customer.get_last_name(), customer.get_email(),
                                 customer.get_phone(), customer.get_address()))
            self.conn.commit()

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error adding customer: {str(e)}")

    def retrieve_customer(self, customer_id):
        try:
            # Retrieve customer information from the database based on CustomerID
            self.cursor.execute("SELECT * FROM customers WHERE CustomerID = %s", (customer_id,))
            customer_data = self.cursor.fetchone()
            if customer_data:
                # Create a Customers object and return it
                return Customers(*customer_data)
            else:
                raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error retrieving customer: {str(e)}")

    def delete_customer(self, customer_id):
        try:
            # Check if the customer with the specified CustomerID exists
            self.cursor.execute("SELECT * FROM customers WHERE CustomerID = %s", (customer_id,))
            existing_customer = self.cursor.fetchone()
            if not existing_customer:
                raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

            # Delete the customer from the database
            self.cursor.execute("DELETE FROM customers WHERE CustomerID = %s", (customer_id,))
            self.conn.commit()

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error deleting customer: {str(e)}")
