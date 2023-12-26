from entity.customers import Customers
from entity.product import Products
from entity.orders import Orders
from entity.orderdetails import OrderDetails
from dao.customers_manager import CustomerManager
from dao.products_manager import ProductManager
from dao.orders_manager import OrderManager

def main():
    # Create instances of managers
    customer_manager = CustomerManager()
    product_manager = ProductManager()
    order_manager = OrderManager()

    try:
        # Add a customer
        customer1 = Customers(1, "John", "Doe", "john.doe@example.com", "123456789", "123 Main St")
        customer_manager.add_customer(customer1)

        # Display customer information
        retrieved_customer = customer_manager.retrieve_customer(1)
        print("Customer Information:")
        print(retrieved_customer.get_customer_details())

        # Add a product
        product1 = Products(1, "Laptop", "High-performance laptop", 999.99)
        product_manager.add_product(product1)



        # Place an order
        order1 = Orders(1, retrieved_customer, "2023-12-16")
        order_detail1 = OrderDetails(1, order1, product1, 2)
        order1.add_order_detail(order_detail1)

        # Display order details
        print("\nOrder Details:")
        # print(order_manager.get_order_details(order1.get_order_id()))


    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        del customer_manager
        del product_manager
        del order_manager

if __name__ == "__main__":
    main()
