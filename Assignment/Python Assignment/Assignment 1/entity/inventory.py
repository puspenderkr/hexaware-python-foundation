from exceptions.exception import InsufficientStockException

# Inventory class with Composition
class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update

    @property
    def inventory_id(self):
        return self.__inventory_id

    @property
    def product(self):
        return self.__product

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @property
    def last_stock_update(self):
        return self.__last_stock_update

    def add_to_inventory(self, quantity):
        if isinstance(quantity, int) and quantity > 0:
            self.__quantity_in_stock += quantity

    def remove_from_inventory(self, quantity):
        if quantity > self.quantity_in_stock:
            raise InsufficientStockException("Not enough stock to fulfill the order")
        if isinstance(quantity, int) and quantity > 0:
            self.__quantity_in_stock -= quantity

    def update_stock_quantity(self, new_quantity):
        if isinstance(new_quantity, int) and new_quantity >= 0:
            self.__quantity_in_stock = new_quantity

    def is_product_available(self, quantity_to_check):
        return self.__quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.__quantity_in_stock * self.product.price

    def list_low_stock_products(self, threshold):
        if self.__quantity_in_stock < threshold:
            return self.product.get_product_details()

    def list_out_of_stock_products(self):
        if self.__quantity_in_stock == 0:
            return self.product.get_product_details()

    def list_all_products(self):
        return self.product.get_product_details()
