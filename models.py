# models.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn})"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User(name={self.name}, user_id={self.user_id})"


class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        return f"Checkout(user_id={self.user_id}, isbn={self.isbn})"
