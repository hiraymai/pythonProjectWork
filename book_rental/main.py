from user import UserManager
from book import Book
from rental_service import RentalService
from storage import save_books_json, load_books_json, save_users_csv, load_users_csv

def main():
    user_manager = load_users_csv()
    rental_service = RentalService()
    rental_service.books = load_books_json()

    while True:
        action = input("Choose action (login, register, add_book, rent_book, view_receipts, exit): ").strip().lower()
        if action == "login":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if user_manager.authenticate(username, password):
                print("Login successful.")
            else:
                print("Login failed.")
        elif action == "register":
            try:
                username = input("Choose a username: ").strip()
                password = input("Choose a password: ").strip()
                user_manager.add_user(username, password)
                print("User registered successfully.")
            except ValueError as e:
                print(e)
        elif action == "add_book":
            # This section assumes the user is logged in or validation is handled elsewhere
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            year = input("Year: ").strip()
            isbn = input("ISBN: ").strip()
            book = Book(title, author, year, isbn)
            rental_service.add_book(book)
            print("Book added successfully.")
        elif action == "rent_book":
            isbn = input("Enter ISBN of the book to rent: ").strip()
            username = input("Enter your username: ").strip()
            receipt = rental_service.rent_book(username, isbn)
            if receipt:
                print("Book rented successfully.")
            else:
                print("Book not found.")
        elif action == "view_receipts":
            username = input("Enter your username to view your rental receipts: ").strip()
            receipts = rental_service.filter_receipts(username)
            for receipt in receipts:
                print(receipt)
        elif action == "exit":
            save_users_csv(user_manager, 'users.csv')
            save_books_json(rental_service.books, 'books.json')
            print("Exiting and saving data...")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
