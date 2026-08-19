class Cinema:
    def __init__(self):
        self.movies = []
        self.customers = []
        self.booking = []


class Movie:
    def __init__(self, movie_id, movie_name, genre, duration, price):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.genre = genre
        self.duration = duration
        self.price = price


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email


class Booking:
    def __init__(self, booking_id, customer, movie, seat_no, quantity, total_price):
        self.booking_id = booking_id
        self.customer = customer
        self.movie = movie
        self.seat_no = seat_no
        self.quantity = quantity
        self.total_price = total_price
        self.status = "booked"