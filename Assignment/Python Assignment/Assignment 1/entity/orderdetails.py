from exceptions.exception import IncompleteOrderException
class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        if not product:
            raise IncompleteOrderException("Order detail lacks a product reference")
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @property
    def order(self):
        return self.__order

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    def calculate_subtotal(self):
        return self.product.price * self.__quantity

    def get_order_detail_info(self):
        return f"OrderDetailID: {self.order_detail_id}, Product: {self.product.get_product_details()}, Quantity: {self.quantity}"

    def update_quantity(self, new_quantity):
        if isinstance(new_quantity, int) and new_quantity > 0:
            self.__quantity = new_quantity

    def add_discount(self, discount):
        # Logic to apply discount
        pass
