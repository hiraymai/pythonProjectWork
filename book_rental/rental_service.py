# Rental Service Core
from datetime import datetime
from book import Book

# Data structure
class RentalReceipt:
    def __init__(self, username, book, rental_date):
        self.username = username
        self.book = book
        self.rental_date = rental_date

    def __str__(self):
        return f"Rented by {self.username} on {self.rental_date}: {self.book}"

class RentalService:
    def __init__(self):
        self.books = []
        self.rentals = []
    def add_book(self, book):
        self.books.append(book)

    def rent_book(self, username, isbn):
        for book in self.books:
            if book.isbn == isbn:
                rental_date = datetime.now().strftime('%Y-%m-%d')
                receipt = RentalReceipt(username, book, rental_date)
                self.rentals.append(receipt)
                return receipt
        return None

    def filter_receipts(self, username):
        return [receipt for receipt in self.rentals if receipt.username == username]
