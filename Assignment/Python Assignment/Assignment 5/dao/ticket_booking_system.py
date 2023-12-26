from entity.movie import Movie
from entity.concert import Concert
from entity.sports import Sports
from decimal import Decimal
from util.database_connector import DBConnection

class TicketBookingSystem:
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    @classmethod
    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue_name):
        try:
            query = "INSERT INTO events (event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (event_name, date, time, venue_name, total_seats, total_seats, ticket_price, event_type)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Event created and added to the database successfully.")
        except Exception as e:
            print(f"Error creating event and adding to the database: {e}")
            self.conn.rollback()

    @classmethod
    def display_event_details(self, event_id):
        try:
            query = "SELECT * FROM events WHERE event_id = %s"
            values = (event_id,)
            self.cursor.execute(query, values)
            event = self.cursor.fetchone()

            if event:
                print("Event Details:")
                print(f"Event Name: {event[1]}")
                print(f"Event Date: {event[2]}")
                print(f"Event Time: {event[3]}")
                print(f"Venue Name: {event[4]}")
                print(f"Total Seats: {event[5]}")
                print(f"Available Seats: {event[6]}")
                print(f"Ticket Price: {event[7]}")
                print(f"Event Type: {event[8]}")
            else:
                print("Event not found.")
        except Exception as e:
            print(f"Error displaying event details: {e}")

    @classmethod
    def book_tickets(self, event_id, num_tickets):
        try:
            query_select = "SELECT available_seats, ticket_price FROM events WHERE event_id = %s"
            values_select = (event_id,)
            self.cursor.execute(query_select, values_select)
            event_data = self.cursor.fetchone()

            if event_data:
                available_seats, ticket_price = event_data
                if num_tickets <= available_seats:
                    total_cost = num_tickets * ticket_price

                    query_update = "UPDATE events SET available_seats = available_seats - %s WHERE event_id = %s"
                    values_update = (num_tickets, event_id)
                    self.cursor.execute(query_update, values_update)
                    self.conn.commit()

                    print(f"Booked {num_tickets} tickets for the event. Total Cost: {total_cost}")
                else:
                    print("Not enough available seats.")
            else:
                print("Event not found.")
        except Exception as e:
            print(f"Error booking tickets: {e}")
            self.conn.rollback()

    @classmethod
    def cancel_tickets(self, event_id, num_tickets):
        try:
            query_update = "UPDATE events SET available_seats = available_seats + %s WHERE event_id = %s"
            values_update = (num_tickets, event_id)
            self.cursor.execute(query_update, values_update)
            self.conn.commit()

            print(f"Cancelled booking for {num_tickets} tickets.")
        except Exception as e:
            print(f"Error cancelling tickets: {e}")
            self.conn.rollback()


    @classmethod
    def main(cls):
        while True:
            print("1. Create Event")
            print("2. Display Event Details")
            print("3. Book Tickets")
            print("4. Cancel Tickets")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                event_name = input("Enter event name: ")
                date = input("Enter date (YYYY-MM-DD): ")
                time_str = input("Enter time (HH:MM): ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Sports/Concert): ")
                if event_type not in ['Movie', 'Sports', 'Concert'] :
                    raise ValueError("Invalid event type")
                venue_name = input("Enter venue name: ")

                cls.create_event(event_name, date, time_str, total_seats, ticket_price, event_type, venue_name)

            elif choice == '2':
                if cls.events:
                    event = cls.events[int(input("Enter event index: "))]
                    cls.display_event_details(event)
                else:
                    print("No events created yet.")

            elif choice == '3':
                if cls.events:
                    event = cls.events[int(input("Enter event index: "))]
                    num_tickets = int(input("Enter number of tickets to book: "))
                    cls.book_tickets(event, num_tickets)
                else:
                    print("No events created yet.")

            elif choice == '4':
                if cls.events:
                    event = cls.events[int(input("Enter event index: "))]
                    num_tickets = int(input("Enter number of tickets to cancel: "))
                    cls.cancel_tickets(event, num_tickets)
                else:
                    print("No events created yet.")

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")