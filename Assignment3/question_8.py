''''
A program to implement a basic library book management 
'''
import csv
import os

class Book:
    """
    Represents a Book in the Library.
    """
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def get_details(self):
        """
        Returns book details as a list.
        """
        return [self.book_id, self.title, self.author, "Available" if self.available else "Issued"]

class Library:
    """
    Represents the Library with functionalities to manage books.
    """
    def __init__(self, filename="books.csv"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """
        Loads books from the CSV file into the program.
        """
        try:
            if os.path.exists(self.filename):
                with open(self.filename, mode="r", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    next(reader, None)  # Skip header
                    self.books = [Book(row[0], row[1], row[2], row[3] == "Available") for row in reader]
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        """
        Saves the current book list to the CSV file.
        """
        try:
            with open(self.filename, mode="w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Book ID", "Title", "Author", "Status"])  # Header
                for book in self.books:
                    writer.writerow(book.get_details())
        except Exception as e:
            print(f"Error saving books: {e}")

    def add_book(self, book):
        """
        Adds a new book to the library.
        """
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added successfully!")

    def issue_book(self, book_id):
        """
        Issues a book if available.
        """
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    self.save_books()
                    print(f"Book '{book.title}' has been issued.")
                    return
                else:
                    print("Sorry, this book is already issued.")
                    return
        print("Book not found!")

    def return_book(self, book_id):
        """
        Returns a book to the library.
        """
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    self.save_books()
                    print(f"Book '{book.title}' has been returned.")
                    return
                else:
                    print("This book was not issued.")
                    return
        print("Book not found!")

    def search_book(self, keyword):
        """
        Searches for books by title or author.
        """
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        
        if found_books:
            print("\n--- Search Results ---")
            for book in found_books:
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {'Available' if book.available else 'Issued'}")
        else:
            print("No books found with that keyword!")

# Main program loop
library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        new_book = Book(book_id, title, author)
        library.add_book(new_book)
    
    elif choice == "2":
        book_id = input("Enter Book ID to issue: ")
        library.issue_book(book_id)

    elif choice == "3":
        book_id = input("Enter Book ID to return: ")
        library.return_book(book_id)

    elif choice == "4":
        keyword = input("Enter title or author to search: ")
        library.search_book(keyword)
    
    elif choice == "5":
        print("Exiting Library Management System. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a valid option.")
