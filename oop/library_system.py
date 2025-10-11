# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        #Base class for all books
        self.title = title
        self.author = author

    def __str__(self):
        # FIX: Added "Book: " prefix and removed quotes around {self.title}
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        #EBook derived from Book, with file size in MB
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        # FIX: Removed quotes, changed "File size" to "File Size", and "MB" to "KB"
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        #PrintBook derived from Book, with page count
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        # FIX: Removed quotes and changed "Pages" to "Page Count"
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        #Library uses composition to hold books
        self.books = []

    def add_book(self, book: Book):
        #Add a book (Book, EBook, or PrintBook) to the collection
        self.books.append(book)

    def list_books(self):
        #List all books in the library
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the Library:")
            for book in self.books:
                # FIX: Removed the " - " prefix
                print(book)