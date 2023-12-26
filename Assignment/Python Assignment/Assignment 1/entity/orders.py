from exceptions.exception import IncompleteOrderException, InsufficientStockException

class Orders:
    def __init__(self, order_id, customer, order_date):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.order_details = []

    def get_order_id(self):
        return self.order_id

    def get_customer(self):
        return self.customer

    def get_order_date(self):
        return self.order_date

    def get_order_details(self):
        return self.order_details

    def add_order_detail(self, order_detail):
        self.order_details.append(order_detail)

    def calculate_total_amount(self):
        return sum(order_detail.calculate_subtotal() for order_detail in self.order_details)

    def get_order_details_info(self):
        details_info = "\n".join(order_detail.get_order_detail_info() for order_detail in self.order_details)
        return f"Order ID: {self.order_id}\n" \
               f"Order Date: {self.order_date}\n" \
               f"Total Amount: ${self.calculate_total_amount()}\n" \
               f"Order Details:\n{details_info}"

    def calculate_total_amount(self):
        self.__total_amount = sum(detail.calculate_subtotal() for detail in self.__order_details)

    def get_order_details(self):
        details = [f"{detail.product.product_name} - Quantity: {detail.quantity}" for detail in self.__order_details]
        return f"OrderID: {self.order_id}, Customer: {self.customer.get_customer_details()}, Order Date: {self.order_date}, Total Amount: {self.total_amount}, Order Details: {', '.join(details)}"

    def update_order_status(self, new_status):
        # Logic to update order status
        pass

    def cancel_order(self):
        try:
            # Logic to cancel order and adjust stock levels
            for detail in self.__order_details:
                detail.product.remove_from_inventory(detail.quantity)
        except InsufficientStockException as e:
            # Handle insufficient stock exception
            print(f"Error canceling order: {e}")
