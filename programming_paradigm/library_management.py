# **LIBRARY MANAGEMENT SYSTEM**

class Book:           # Define class
    def __init__(self, title, author):
        self.title = title            # Public attribute
        self.author = author          # Public attribute
        self.__is_checked_out = False # Private attribute

    def check_out(self):
        self.__is_checked_out = True  # Marks the book as checked out

    def return_book(self):
        self.__is_checked_out = False # Marks the book as returned (available)
    def is_checked_out(self):
        return self.__is_checked_out  # Return True if the book is checked out False otherwise.
    
class Library:
    def __init__(self):
        self._books = []             # Private attribute to hold Book object

    def add_book(self, book):
        self._books.append(book)         # Add Book instance to the library

    def check_out_book(self, title):  # Checks out the book with the given title if available
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return
        print(f"Book {title} isn't available for chek out")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return
        print(f"Book {title} was not checked out or doesn't exist")
    
    def list_available_books(self):
        available = False
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
                available = True
        if not available:
            print("No books available.")
    





