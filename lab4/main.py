"""
formatted code
"""

available_books = []
borrowed_books = []


def add_book(name, year, author):
    """
    add book to library
    """
    available_books.append({"name": name, "year": year, "author": author})


def borrow_book(name, year, author):
    """
    borrow book from library
    """
    available_books.remove({"name": name, "year": year, "author": author})
    borrowed_books.append({"name": name, "year": year, "author": author})


def list_available_books():
    """
    list available books
    """
    for book in available_books:
        print(book["name"], book["year"], book["author"])


def list_borrowed_books():
    """
    list borrowed books
    """
    for book in borrowed_books:
        print(book["name"], book["year"], book["author"])


def return_book(name, year, author):
    """
    return book to library
    """
    borrowed_books.remove({"name": name, "year": year, "author": author})
    available_books.append({"name": name, "year": year, "author": author})


add_book("Harry Potter", 1997, "J.K. Rowling")
add_book("The Lord of the Rings", 1954, "J.R.R. Tolkien")
add_book("The Hobbit", 1937, "J.R.R. Tolkien")
add_book("The Chronicles of Narnia", 1950, "C.S. Lewis")
add_book("The Lion, the Witch and the Wardrobe", 1950, "C.S. Lewis")
add_book("The Two Towers", 1954, "J.R.R. Tolkien")
print("Available books: ")
list_available_books()
print("\nBorrowed books: ")
list_borrowed_books()
borrow_book("Harry Potter", 1997, "J.K. Rowling")
borrow_book("The Lord of the Rings", 1954, "J.R.R. Tolkien")
borrow_book("The Hobbit", 1937, "J.R.R. Tolkien")
print("\nAvailable books: ")
list_available_books()
print("\nBorrowed books: ")
list_borrowed_books()
return_book("Harry Potter", 1997, "J.K. Rowling")
return_book("The Lord of the Rings", 1954, "J.R.R. Tolkien")
print("\nAvailable books: ")
list_available_books()
print("\nBorrowed books: ")
list_borrowed_books()
