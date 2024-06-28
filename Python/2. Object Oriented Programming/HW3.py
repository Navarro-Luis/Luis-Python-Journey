class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {availability}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available for borrowing")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} has not borrowed '{book.title}'")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"{self.name} (ID: {self.member_id}) - Borrowed Books: {borrowed_titles}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library")

    def __str__(self):
        books_str = "\n".join(str(book) for book in self.books)
        members_str = "\n".join(str(member) for member in self.members)
        return f"{self.name}\nBooks:\n{books_str}\nMembers:\n{members_str}"
    
    # Example Usage

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("1984", "George Orwell", "0987654321")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "1122334455")

# Create members
member1 = Member("Alice Johnson", "M001")
member2 = Member("Bob Smith", "M002")

# Create library
library = Library("Central Library")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add members to library
library.add_member(member1)
library.add_member(member2)

# Borrow and return books
member1.borrow_book(book1)
member2.borrow_book(book2)

# Print status
print(library)

# Return books
member1.return_book(book1)
member2.return_book(book2)

# Print status again
print(library)