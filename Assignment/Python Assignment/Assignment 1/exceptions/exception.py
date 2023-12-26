class InvalidDataException(Exception):
    def __init__(self, message="Invalid data entered"):
        self.message = message
        super().__init__(self.message)

class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock for this product"):
        self.message = message
        super().__init__(self.message)

class IncompleteOrderException(Exception):
    def __init__(self, message="Incomplete order details: Product reference is missing"):
        self.message = message
        super().__init__(self.message)

class PaymentFailedException(Exception):
    def __init__(self, message="Payment processing failed"):
        self.message = message
        super().__init__(self.message)

class FileIOException(Exception):
    def __init__(self, message="Error during file I/O"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Error connecting to the database"):
        self.message = message
        super().__init__(self.message)

class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency issue: Data update conflict"):
        self.message = message
        super().__init__(self.message)

class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed"):
        self.message = message
        super().__init__(self.message)

class AuthorizationException(Exception):
    def __init__(self, message="Unauthorized access"):
        self.message = message
        super().__init__(self.message)

class DuplicateProductException(Exception):
    def __init__(self, message="Duplicate Product"):
        self.message = message
        super().__init__(self.message)

class InvalidUpdateException(Exception):
    def __init__(self, message="Invalid Update entered"):
        self.message = message
        super().__init__(self.message)

class ProductInOrderException(Exception):
    def __init__(self, message="Product not in order"):
        self.message = message
        super().__init__(self.message)

class DuplicateCustomerException(Exception):
    def __init__(self, message="Duplicate Customer"):
        self.message = message
        super().__init__(self.message)

class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer Not Found"):
        self.message = message
        super().__init__(self.message)

class OrderUpdateException(Exception):
    def __init__(self, message="Invalid Order Update entered"):
        self.message = message
        super().__init__(self.message)

