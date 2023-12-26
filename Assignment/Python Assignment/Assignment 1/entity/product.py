# products.py

class Products:
    def __init__(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_product_details(self):
        return f"Product ID: {self.product_id}\n" \
               f"Product Name: {self.product_name}\n" \
               f"Description: {self.description}\n" \
               f"Price: ${self.price}"
