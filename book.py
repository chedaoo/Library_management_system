# book.py
from models import Book
import storage

class BookManager:
    def __init__(self):
        self.books = storage.load_books()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        storage.save_books(self.books)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book(self, **kwargs):
        for book in self.books:
            if all(getattr(book, k) == v for k, v in kwargs.items()):
                return book
        return None
