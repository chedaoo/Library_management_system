# Library Management System

This project is a simple Library Management System implemented in Python. It allows users to manage books and users, check out and check in books, and track book availability. The application is designed using Object-Oriented Programming principles and utilizes file-based storage for persistent data.

## Features

1. **Manage Books**: Add, update, delete, list, and search books by various attributes like title, author, or ISBN.
2. **Manage Users**: Add, update, delete, list, and search users by attributes like name and user ID.
3. **Check Out and Check In Books**: Record when books are checked out and returned by users.
4. **Track Book Availability**: Ensure books are available or checked out.
5. **Simple Logging**: Log operations for auditing purposes.

## Project Structure

The project consists of the following files:
.
├── book.py
├── check.py
├── main.py
├── models.py
├── storage.py
└── user.py

### `models.py`

Defines the core classes for the Library Management System:

- `Book`: Represents a book with attributes `title`, `author`, and `isbn`.
- `User`: Represents a user with attributes `name` and `user_id`.
- `Checkout`: Represents a checkout record with attributes `user_id` and `isbn`.

### `book.py`

Contains the `BookManager` class which handles book-related operations:

- `add_book(title, author, isbn)`: Adds a new book.
- `list_books()`: Lists all books.
- `find_book(**kwargs)`: Finds a book by given attributes.

### `user.py`

Contains the `UserManager` class which handles user-related operations:

- `add_user(name, user_id)`: Adds a new user.
- `list_users()`: Lists all users.
- `find_user(**kwargs)`: Finds a user by given attributes.

### `check.py`

Contains the `CheckoutManager` class which handles checkout-related operations:

- `checkout_book(user_id, isbn)`: Records a book checkout.
- `list_checkouts()`: Lists all checkout records.

### `storage.py`

Handles file-based storage using JSON:

- `load_books()`: Loads books from the JSON file.
- `save_books(books)`: Saves books to the JSON file.
- `load_users()`: Loads users from the JSON file.
- `save_users(users)`: Saves users to the JSON file.
- `load_checkouts()`: Loads checkouts from the JSON file.
- `save_checkouts(checkouts)`: Saves checkouts to the JSON file.

### `main.py`

Provides a command-line interface for interacting with the Library Management System:

- Displays a menu with options to add books, list books, add users, and check out books.
- Interacts with `BookManager`, `UserManager`, and `CheckoutManager` to perform operations.

## Installation and Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. **Run the application**:
    ```bash
    python main.py
    ```

3. **Follow the on-screen instructions** to manage books, users, and checkouts.

## Future Enhancements

The application is designed to be modular and scalable. Future enhancements can include:

- Adding update and delete functionalities for books and users.
- Implementing due dates for books and calculating late fees.
- Enhancing the logging mechanism for better auditing.
- Adding a graphical user interface (GUI) for better user experience.



