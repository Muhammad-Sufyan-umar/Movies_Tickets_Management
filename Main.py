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


class Booking:
    def __init__(self, booking_id, customer, movie, seat_no, quantity, total_price):
        self.booking_id = booking_id
        self.customer = customer
        self.movie = movie
        self.seat_no = seat_no
        self.quantity = quantity
        self.total_price = total_price
        self.status = "booked"