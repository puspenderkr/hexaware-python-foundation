from dao.ticket_booking_system import TicketBookingSystem
from dao.admin import Admin
from entity.customer import Customer
from entity.venue import Venue

if __name__ == "__main__":

    admin = Admin()

    # Creating customer and venue objects
    customer = Customer("John Doe", "john@example.com", "123-456-7890")
    venue = Venue("Cinema Hall", "123 Main St, City")

    # Adding customer and venue to the database
    admin.add_customer_to_database(customer)
    admin.add_venue_to_database(venue)

    TicketBookingSystem.main()
