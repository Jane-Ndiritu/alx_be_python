class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f'Added "{book.title}" by {book.author} to the library.')
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title: str):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f'"{title}" is already checked out.')
                    return
        print(f'Book titled "{title}" not found in the library.')

    def return_book(self, title: str):
        """Return a book by title if it exists in the library."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return
                else:
                    print(f'"{title}" was not checked out.')
                    return
        print(f'Book titled "{title}" not found in the library.')

    def list_available_books(self):
        """List all available books in the library."""
        available = [book for book in self._books if book.is_available()]
        if available:
            print("Available books:")
            for book in available:
                print(f' - "{book.title}" by {book.author}')
        else:
            print("No books are currently available.")
