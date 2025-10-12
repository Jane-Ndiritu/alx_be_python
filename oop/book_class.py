class Book:
    def __init__(self, title: str, author: str, year: int = None):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __del__(self):
        print(f"Deleting book: {self.title}")
