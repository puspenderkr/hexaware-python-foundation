from exceptions.exception import OrderUpdateException
from entity.orders import Orders
from util.database_connector import DBConnection  # Import your DBConnection class

class OrderManager:
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_order(self, order):
        try:
            # Insert the new order into the database
            self.cursor.execute("INSERT INTO orders (OrderID, CustomerID, OrderDate) "
                                "VALUES (%s, %s, %s)",
                                (order.get_order_id(), order.get_customer().get_customer_id(),
                                 order.get_order_date()))
            self.conn.commit()

            # Update inventory and payment records as needed
            # (This part should be implemented based on your specific business logic)

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error adding order: {str(e)}")

    def update_order_status(self, order_id, new_status):
        try:
            # Check if the order with the specified OrderID exists
            self.cursor.execute("SELECT * FROM orders WHERE OrderID = %s", (order_id,))
            existing_order = self.cursor.fetchone()
            if not existing_order:
                raise OrderUpdateException("Order with the specified ID does not exist.")

            # Update the order status in the database
            self.cursor.execute("UPDATE orders SET OrderStatus = %s WHERE OrderID = %s",
                                (new_status, order_id))
            self.conn.commit()

            # Update inventory and payment records as needed
            # (This part should be implemented based on your specific business logic)

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error updating order status: {str(e)}")

    def remove_canceled_order(self, order_id):
        try:
            # Check if the order with the specified OrderID exists
            self.cursor.execute("SELECT * FROM orders WHERE OrderID = %s", (order_id,))
            existing_order = self.cursor.fetchone()
            if not existing_order:
                raise OrderUpdateException("Order with the specified ID does not exist.")

            # Remove the order from the database
            self.cursor.execute("DELETE FROM orders WHERE OrderID = %s", (order_id,))
            self.conn.commit()

            # Update inventory and payment records as needed
            # (This part should be implemented based on your specific business logic)

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error removing canceled order: {str(e)}")

    def sort_orders_by_date_asc(self):
        # Sort orders by order date in ascending order
        self.orders_list.sort(key=lambda order: order.get_order_date())

    def sort_orders_by_date_desc(self):
        # Sort orders by order date in descending order
        self.orders_list.sort(key=lambda order: order.get_order_date(), reverse=True)

    def retrieve_orders_by_date_range(self, start_date, end_date):
        # Retrieve and display orders based on a specific date range
        filtered_orders = [order for order in self.orders_list
                           if start_date <= order.get_order_date() <= end_date]
        return filtered_orders
