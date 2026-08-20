class Cinema:
    def __init__(self):
        self.movies = []
        self.customers = []
        self.booking = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print("Movie added successfully ✅")


    def remove_movie(self, movie):
        self.movies.remove(movie)
        print("Movie removed successfully ✅")


    def search_movie(self, movie_id):
        if self.movies:
            for i in self.movies:
                if i.movie_id == movie_id:
                    print("Movie found")
                    i.show_info()
                    return i

            print("Movie not found..")
        else:
            print("No Movies Yet..")


    def display_movies(self):
        if self.movies:
            for i in self.movies:
                i.show_info()
        else:
            print("No Movies Yet!!!")

	
    def add_customer(self, customer):
        self.customers.append(customer)
        print("Customer added successfully..")


    def search_customer(self, customer_id):
        if self.customers:
            for i in self.customers:
                if i.customer_id == customer_id:
                    print("Customer Found..")
                    i.show_info()
                    return i

            print("Customer Not found")
        else:
            print("No Customer Yet")


    def display_customers(self):
        if self.customers:
            for i in self.customers:
                i.show_info()
        else:
            print("No Customer Yet!!!")

    def book_ticket(self, ticket_info):
        self.booking.append(ticket_info)
        print("Ticket Booked successfully ✔")



    def display_bookings(self):
        if self.booking:
            for i in self.booking:
                i.show_booking()
        else:
            print("No Booking yet...")


    def cancel_ticket(self, ticket_info):
        if ticket_info in self.booking:
            ticket_info.cancel_booking()
        else:
            print("Booking not found..")

class Movie:
    def __init__(self, movie_id, movie_name, genre, duration, price):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.genre = genre
        self.duration = duration
        self.price = price

    def show_info(self):
        print(
            f"ID : {self.movie_id} | "
            f"Name: {self.movie_name} | "
            f"Genre : {self.genre} | "
            f"Duration : {self.duration} | "
            f"Price : {self.price}"
        )

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def show_info(self):
        print(
            f"ID : {self.customer_id} | "
            f"Name : {self.name} | "
            f"Email : {self.email}"
        )


class Booking:
    def __init__(self, booking_id, customer, movie, seat_no, quantity, total_price):
        self.booking_id = booking_id
        self.customer = customer
        self.movie = movie
        self.seat_no = seat_no
        self.quantity = quantity
        self.total_price = total_price
        self.status = "booked"

    def calculate_total(self):
        self.total_price = self.movie.price * self.quantity
        return self.total_price

    def show_booking(self):
        print(
            f"ID : {self.booking_id} | "
            f"Customer : {self.customer.name} | "
            f"Movie : {self.movie.movie_name} | "
            f"Seat_No : {self.seat_no} | "
            f"Quantity : {self.quantity} | "
            f"Total Price : {self.total_price} | "
            f"Status : {self.status}"
        )

    def cancel_booking(self):
        if self.status == "booked":
            self.status = "cancelled"
            print(
                f"Booking {self.booking_id} "
                f"cancelled successfully.."
            )
        else:
            print("Booking already cancelled")