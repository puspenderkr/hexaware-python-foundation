from enum import Enum

class EventType(Enum):
    MOVIE = 'Movie'
    SPORTS = 'Sports'
    CONCERT = 'Concert'

class Event:
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = EventType(event_type)

    def calculate_total_revenue(self):
        return self.total_seats * self.ticket_price

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"Booked {num_tickets} tickets for {self.event_name}")
        else:
            print("Not enough available seats.")

    def cancel_booking(self, num_tickets):
        if num_tickets <= self.get_booked_no_of_tickets():
            self.available_seats += num_tickets
            print(f"Cancelled booking for {num_tickets} tickets for {self.event_name}")
        else:
            print("Invalid number of tickets to cancel.")

    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Time: {self.event_time}")
        print(f"Venue Name: {self.venue_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type.value}")

