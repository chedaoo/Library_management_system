# storage.py
import json
from models import Book, User, Checkout

BOOKS_FILE = 'books.json'
USERS_FILE = 'users.json'
CHECKOUTS_FILE = 'checkouts.json'

def load_books():
    try:
        with open(BOOKS_FILE, 'r') as file:
            books_data = json.load(file)
            return [Book(**data) for data in books_data]
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump([book.__dict__ for book in books], file)

def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            users_data = json.load(file)
            return [User(**data) for data in users_data]
    except FileNotFoundError:
        return []

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump([user.__dict__ for user in users], file)

def load_checkouts():
    try:
        with open(CHECKOUTS_FILE, 'r') as file:
            checkouts_data = json.load(file)
            return [Checkout(**data) for data in checkouts_data]
    except FileNotFoundError:
        return []

def save_checkouts(checkouts):
    with open(CHECKOUTS_FILE, 'w') as file:
        json.dump([checkout.__dict__ for checkout in checkouts], file)
