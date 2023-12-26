from exceptions.exception import DuplicateProductException, InvalidUpdateException, ProductInOrderException
from entity.product import Products
from util.database_connector import DBConnection

class ProductManager:
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_product(self, product):
        try:
            # Check if the product with the same ProductID or ProductName already exists
            self.cursor.execute("SELECT * FROM products WHERE ProductID = %s OR ProductName = %s",
                                (product.get_product_id(), product.get_product_name()))
            existing_product = self.cursor.fetchone()
            if existing_product:
                raise DuplicateProductException("Product with the same ID or Name already exists.")

            # Insert the new product into the database
            self.cursor.execute("INSERT INTO products (ProductID, ProductName, Description, Price) "
                                "VALUES (%s, %s, %s, %s)",
                                (product.get_product_id(), product.get_product_name(),
                                 product.get_description(), product.get_price()))
            self.conn.commit()

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error adding product: {str(e)}")

    def update_product(self, product):
        try:
            # Check if the product with the specified ProductID exists
            self.cursor.execute("SELECT * FROM products WHERE ProductID = %s", (product.get_product_id(),))
            existing_product = self.cursor.fetchone()
            if not existing_product:
                raise InvalidUpdateException("Product with the specified ID does not exist.")

            # Update the product in the database
            self.cursor.execute("UPDATE products SET ProductName = %s, Description = %s, Price = %s "
                                "WHERE ProductID = %s",
                                (product.get_product_name(), product.get_description(),
                                 product.get_price(), product.get_product_id()))
            self.conn.commit()

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error updating product: {str(e)}")

    def remove_product(self, product_id):
        try:
            # Check if the product is associated with any order
            self.cursor.execute("SELECT * FROM orderdetails WHERE ProductID = %s", (product_id,))
            existing_order_detail = self.cursor.fetchone()
            if existing_order_detail:
                raise ProductInOrderException("Cannot remove product associated with existing orders.")

            # Remove the product from the database
            self.cursor.execute("DELETE FROM products WHERE ProductID = %s", (product_id,))
            self.conn.commit()

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error removing product: {str(e)}")
