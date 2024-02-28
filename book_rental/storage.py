# Data Storage
import json
import csv
from book import Book
from user import User, UserManager

# JSON for books
def save_books_json(books, filepath='books.json'):
    with open(filepath, 'w') as file:
        json.dump([vars(book) for book in books], file)

def load_books_json(filepath='books.json'):
    books = []
    try:
        with open(filepath, 'r') as file:
            books_data = json.load(file)
            for data in books_data:
                books.append(Book(**data))
    except FileNotFoundError:
        pass
    return books

# CSV for users
def save_users_csv(user_manager, filepath='users.csv'):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        for user in user_manager.users.values():
            writer.writerow([user.username, user.password])

def load_users_csv(filepath='users.csv'):
    user_manager = UserManager()
    try:
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                user_manager.add_user(row[0], row[1])
    except FileNotFoundError:
        pass
    return user_manager

