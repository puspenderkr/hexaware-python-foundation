from sortedcontainers import SortedList
from exceptions import ProductNotFoundException
from entity.inventory import Inventory
from entity.product import Products
from util.database_connector import DBConnection  # Import your DBConnection class

class InventoryManager:
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()
        self.inventory_list = SortedList(key=lambda inventory: inventory.get_product().get_product_id())

    def __del__(self):
        self.conn.close()

    def add_to_inventory(self, product, quantity):
        try:
            # Check if the product is already in the inventory
            existing_inventory = self.inventory_list.find(product.get_product_id())
            if existing_inventory:
                existing_inventory.update_quantity(existing_inventory.get_quantity_in_stock() + quantity)
            else:
                # Insert a new inventory item
                new_inventory = Inventory(product=product, quantity_in_stock=quantity, last_stock_update=None)
                self.inventory_list.add(new_inventory)

                # Insert the new inventory item into the database
                self.cursor.execute("INSERT INTO inventory (ProductID, QuantityInStock, LastStockUpdate) "
                                    "VALUES (%s, %s, %s)",
                                    (product.get_product_id(), quantity, None))
                self.conn.commit()

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error updating inventory: {str(e)}")

    def remove_from_inventory(self, product_id, quantity):
        try:
            # Check if the product is in the inventory
            existing_inventory = self.inventory_list.find(product_id)
            if existing_inventory:
                # Check if there is enough quantity in stock
                if existing_inventory.get_quantity_in_stock() >= quantity:
                    existing_inventory.update_quantity(existing_inventory.get_quantity_in_stock() - quantity)
                else:
                    raise ValueError("Insufficient quantity in stock.")

                # Update the inventory item in the database
                self.cursor.execute("UPDATE inventory SET QuantityInStock = %s WHERE ProductID = %s",
                                    (existing_inventory.get_quantity_in_stock(), product_id))
                self.conn.commit()

            else:
                raise ProductNotFoundException("Product not found in inventory.")

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error updating inventory: {str(e)}")

    def get_inventory_info(self):
        return [(inventory.get_product().get_product_name(), inventory.get_quantity_in_stock())
                for inventory in self.inventory_list]

    def is_product_available(self, product_id, quantity_to_check):
        try:
            # Check if the product is in the inventory
            existing_inventory = self.inventory_list.find(product_id)
            if existing_inventory:
                return existing_inventory.get_quantity_in_stock() >= quantity_to_check
            else:
                raise ProductNotFoundException("Product not found in inventory.")

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error checking product availability: {str(e)}")
            return False
        
    def update_inventory_on_order_processing(self, order_details_list):
        try:
            for order_detail in order_details_list:
                product_id = order_detail.get_product().get_product_id()
                quantity_to_remove = order_detail.get_quantity()

                # Check if the product with the specified ProductID exists in inventory
                if product_id in self.inventory_list:
                    existing_inventory = self.inventory_list[product_id]

                    # Check if there are enough quantities in stock
                    if existing_inventory.get_quantity_in_stock() < quantity_to_remove:
                        raise ProductInOrderException(f"Insufficient stock for product {product_id} in order processing.")
                    else:
                        # Update the quantity in inventory and the database
                        existing_inventory.update_stock_quantity(existing_inventory.get_quantity_in_stock() - quantity_to_remove)
                        self.cursor.execute("UPDATE inventory SET QuantityInStock = %s WHERE ProductID = %s",
                                            (existing_inventory.get_quantity_in_stock(), product_id))
                        self.conn.commit()

                else:
                    raise ProductInOrderException(f"Product {product_id} not found in inventory.")

        except Exception as e:
            # Handle database-related exceptions
            print(f"Error updating inventory on order processing: {str(e)}")

