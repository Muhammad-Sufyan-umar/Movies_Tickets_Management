# 🎬 Movie Theater Management System

A simple **Movie Theater Management System** built in Python using **Object-Oriented Programming (OOP)** concepts.

This project allows a cinema to manage movies, customers, and ticket bookings through a simple command-line menu.

## 📌 Features

* 🎬 Add new movies
* 📋 Display all movies
* 🔍 Search movie by Movie ID
* 👤 Add customers
* 📋 Display all customers
* 🎟️ Book movie tickets
* 📋 Display all bookings
* ❌ Cancel booked tickets
* 💰 Automatically calculate total ticket price
* 🚪 Exit the application

## 🧱 Classes Used

### 1. `Cinema`

The main management class responsible for handling:

* Movies
* Customers
* Bookings

Main methods:

* `add_movie()`
* `remove_movie()`
* `search_movie()`
* `display_movies()`
* `add_customer()`
* `search_customer()`
* `display_customers()`
* `book_ticket()`
* `display_bookings()`
* `cancel_ticket()`

### 2. `Movie`

Stores movie information such as:

* Movie ID
* Movie name
* Genre
* Duration
* Ticket price

### 3. `Customer`

Stores customer information:

* Customer ID
* Customer name
* Email

### 4. `Booking`

Handles ticket booking information:

* Booking ID
* Customer
* Movie
* Seat number
* Ticket quantity
* Total price
* Booking status

It also provides methods to:

* Calculate total price
* Display booking information
* Cancel a booking

## 🛠️ OOP Concepts Used

This project demonstrates several Python OOP concepts:

* Classes and Objects
* Constructors (`__init__`)
* Instance Attributes
* Instance Methods
* Object Relationships
* Lists of Objects
* Encapsulation of related functionality
* Basic CRUD-style operations

## 🎟️ Booking Process

The ticket booking process works like this:

1. Enter Booking ID
2. Search for the customer
3. Search for the movie
4. Enter seat number
5. Enter number of tickets
6. Calculate total price
7. Save the booking
8. Display booking details

### 💰 Price Calculation

The total price is calculated using:

```text
Total Price = Movie Price × Number of Tickets
```

For example:

```text
Movie Price = 500
Quantity = 3

Total Price = 500 × 3
            = 1500
```

## 📋 Menu

```text
1. Add Movie
2. Display Movies
3. Search Movie
4. Add Customer
5. Display Customers
6. Book Ticket
7. Display Bookings
8. Cancel Ticket
9. Exit
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone <your-repository-url>
```

Go to the project directory:

```bash
cd <project-folder>
```

Run the Python file:

```bash
python main.py
```

## 💻 Example

```text
1. Add Movie
2. Display Movies
3. Search Movie
4. Add Customer
5. Display Customers
6. Book Ticket
7. Display Bookings
8. Cancel Ticket
9. Exit

Enter choice: 1

Enter Movie id: M101
Enter Movie name: Avengers
Enter genre: Action
Enter duration: 2h 30m
Enter price: 500

Movie added successfully ✅
```

## 🎯 Project Purpose

The purpose of this project is to practice **Python OOP** by building a real-world cinema management system.

It helps demonstrate how multiple classes can work together to manage movies, customers, and ticket bookings.

## 🚀 Future Improvements

Some possible improvements for this project are:

* Add seat availability checking
* Prevent duplicate Movie IDs
* Prevent duplicate Customer IDs
* Prevent duplicate Booking IDs
* Add multiple seats for a booking
* Add different movie show timings
* Add admin login
* Save data permanently using files or a database
* Add payment functionality
* Add a graphical user interface (GUI)

## 👨‍💻 Technologies Used

* **Python 3**
* **Object-Oriented Programming**
* **Command Line Interface (CLI)**

## 📄 License

This project is created for **learning and practice purposes**.
