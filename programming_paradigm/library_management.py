# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title            # public attribute
        self.author = author          # public attribute
        self._is_checked_out = False  # private attribute (convention: underscore)

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []  # private list to store Book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"You have checked out '{title}'."
        return f"'{title}' is not available."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"You have returned '{title}'."
        return f"'{title}' was not checked out."

    def list_available_books(self):
        """List all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            return "\n".join(str(book) for book in available_books)
        return "No books available."


# Example usage
if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    print("Available books:")
    print(library.list_available_books())

    # Check out a book
    print("\n" + library.check_out_book("1984"))
    print("\nAvailable books after checkout:")
    print(library.list_available_books())

    # Return a book
    print("\n" + library.return_book("1984"))
    print("\nAvailable books after return:")
    print(library.list_available_books())