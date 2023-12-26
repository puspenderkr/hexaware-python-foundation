class Booking:
    def __init__(self, event, num_tickets):
        self.event = event
        self.num_tickets = num_tickets
        self.calculate_booking_cost()

    def calculate_booking_cost(self):
        self.total_cost = self.num_tickets * self.event.ticket_price

    def book_tickets(self):
        self.event.book_tickets(self.num_tickets)

    def cancel_booking(self):
        self.event.cancel_booking(self.num_tickets)

    def get_available_no_of_tickets(self):
        return self.event.available_seats

    def get_event_details(self):
        return self.event.display_event_details()

