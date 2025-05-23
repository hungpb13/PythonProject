# Magic method = dunder method (double underscore) __init__, __str__, __eq__
# Automatically called by many of Python's built-in operations
# Allow dev to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book_one = Book("The Lords of the Ring", "J.R.R Tolkien", 1000)
book_two = Book("Harry Potter", "J.K. Rowling", 800)
book_three = Book("The Lords of the Ring", "J.R.R Tolkien", 900)

print(book_one)
print(book_two)

print(book_one == book_three)
print(book_two < book_one)
print(book_two > book_one)

print(f"Total pages = {book_one + book_two}")

print("Ring" in book_three)
print("Rowling" in book_two)

print(book_one['num_pages'])
print(book_one['audio'])
