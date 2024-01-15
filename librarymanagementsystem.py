class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book_id):
        book = library.find_book(book_id)
        if book and book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed {book.title}")
        else:
            print(f"Book with ID {book_id} is not available for borrowing.")

    def return_book(self, library, book_id):
        book = library.find_book(book_id)
        if book and book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has successfully returned {book.title}")
        else:
            print(f"Book with ID {book_id} is not borrowed by {self.name}.")

    def display_borrowed_books(self):
        print(f"{self.name}'s Borrowed Books:")
        for book in self.borrowed_books:
            print(book)


# Example Usage:
if __name__ == "__main__":
    # Create library and books
    library = Library()
    book1 = Book(1, "Introduction to Python", "John Doe")
    book2 = Book(2, "Data Structures and Algorithms", "Jane Smith")
    library.add_book(book1)
    library.add_book(book2)

    # Create members
    member1 = Member(101, "Alice")
    member2 = Member(102, "Bob")

    # Display available books
    print("Available Books in the Library:")
    library.display_books()

    # Alice borrows a book
    member1.borrow_book(library, 1)

    # Bob tries to borrow a non-existent book
    member2.borrow_book(library, 3)

    # Bob borrows a book
    member2.borrow_book(library, 2)

    # Display available books after borrowing
    print("\nAvailable Books in the Library:")
    library.display_books()

    # Display Alice's borrowed books
    member1.display_borrowed_books()

    # Bob returns a book
    member2.return_book(library, 2)

    # Display available books after returning
    print("\nAvailable Books in the Library:")
    library.display_books()

    # Display Bob's borrowed books
    member2.display_borrowed_books()
