# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the eBook."""
        return f"{self.title} by {self.author} (E-Book, {self.file_size}MB)"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"{self.title} by {self.author} (Print Book, {self.page_count} pages)"


class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book (or subclass of Book) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            print("\nBooks currently in the library:")
            for book in self.books:
                print(f"- {book}")
