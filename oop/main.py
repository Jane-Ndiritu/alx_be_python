from book_class import Book
def main():
        # Create a library instance
        my_book = Book("1984", "George Orwell")
        #demonstrating the __str__ method
        print(my_book) #Expected to use the __str__
        #demonstrating the __repr__ method
        print(repr(my_book)) #Expected to use the __repr__
        #deleting the book instance to trigger __del__
        del my_book
        if __name__ == "__main__":
    main()