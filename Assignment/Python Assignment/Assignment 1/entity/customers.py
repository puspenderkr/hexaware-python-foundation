class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_customer_details(self):
        return f"Customer ID: {self.customer_id}\n" \
               f"Name: {self.first_name} {self.last_name}\n" \
               f"Email: {self.email}\n" \
               f"Phone: {self.phone}\n" \
               f"Address: {self.address}"
