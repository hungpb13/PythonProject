# Aggregation = represents a relationship where one object (the whole)
# contains references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("New York Public Library")

book_one = Book("Harry Porter", "J.K. Rowling")
book_two = Book("The Lords of the Ring", "J.R.R. Tolkien")

library.add_book(book_one)
library.add_book(book_two)

print(library.name)
for book in library.list_books():
    print(book)
