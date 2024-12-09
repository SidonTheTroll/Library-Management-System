from db import get_db_connection
from tabulate import tabulate
import datetime

def add_book():
    connection = get_db_connection()
    cursor = connection.cursor()

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    publisher = input("Enter publisher name: ")
    quantity = int(input("Enter quantity: "))

    cursor.execute("INSERT INTO Books (Title, Author, Publisher, Quantity) VALUES (%s, %s, %s, %s)", (title, author, publisher, quantity))
    connection.commit()
    print("Book added successfully!")

    connection.close()

def view_books():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()

    print(tabulate(books, headers=["BookID", "Title", "Author", "Publisher", "Quantity"]))
    connection.close()

def edit_book():
    connection = get_db_connection()
    cursor = connection.cursor()

    book_id = int(input("Enter BookID of the book you want to edit: "))

    # Get current book details
    cursor.execute("SELECT * FROM Books WHERE BookID = %s", (book_id,))
    book = cursor.fetchone()

    if book:
        print(f"Current details: Title: {book[1]}, Author: {book[2]}, Publisher: {book[3]}, Quantity: {book[4]}")
        
        title = input(f"Enter new title (current: {book[1]}): ")
        author = input(f"Enter new author (current: {book[2]}): ")
        publisher = input(f"Enter new publisher (current: {book[3]}): ")
        quantity = input(f"Enter new quantity (current: {book[4]}): ")

        # Update book details
        cursor.execute("""
            UPDATE Books 
            SET Title = %s, Author = %s, Publisher = %s, Quantity = %s 
            WHERE BookID = %s
        """, (title or book[1], author or book[2], publisher or book[3], int(quantity) if quantity else book[4], book_id))

        connection.commit()
        print("Book details updated successfully!")

    else:
        print("Book not found!")

    connection.close()

def add_borrower():
    connection = get_db_connection()
    cursor = connection.cursor()

    name = input("Enter borrower's name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    cursor.execute("INSERT INTO Borrowers (Name, Email, PhoneNumber) VALUES (%s, %s, %s)", (name, email, phone))
    connection.commit()
    print("Borrower added successfully!")

    connection.close()

def view_borrowers():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Borrowers")
    borrowers = cursor.fetchall()

    print(tabulate(borrowers, headers=["BorrowerID", "Name", "Email", "PhoneNumber"]))
    connection.close()

def edit_borrower():
    connection = get_db_connection()
    cursor = connection.cursor()

    borrower_id = int(input("Enter BorrowerID of the borrower you want to edit: "))

    # Get current borrower details
    cursor.execute("SELECT * FROM Borrowers WHERE BorrowerID = %s", (borrower_id,))
    borrower = cursor.fetchone()

    if borrower:
        print(f"Current details: Name: {borrower[1]}, Email: {borrower[2]}, Phone: {borrower[3]}")

        name = input(f"Enter new name (current: {borrower[1]}): ")
        email = input(f"Enter new email (current: {borrower[2]}): ")
        phone = input(f"Enter new phone number (current: {borrower[3]}): ")

        # Update borrower details
        cursor.execute("""
            UPDATE Borrowers 
            SET Name = %s, Email = %s, PhoneNumber = %s 
            WHERE BorrowerID = %s
        """, (name or borrower[1], email or borrower[2], phone or borrower[3], borrower_id))

        connection.commit()
        print("Borrower details updated successfully!")

    else:
        print("Borrower not found!")

    connection.close()

def issue_book():
    connection = get_db_connection()
    cursor = connection.cursor()

    book_id = int(input("Enter BookID to issue: "))
    borrower_id = int(input("Enter BorrowerID: "))
    issue_date = datetime.date.today()

    cursor.execute("INSERT INTO Transactions (BookID, BorrowerID, IssueDate) VALUES (%s, %s, %s)", (book_id, borrower_id, issue_date))
    connection.commit()

    cursor.execute("UPDATE Books SET Quantity = Quantity - 1 WHERE BookID = %s", (book_id,))
    connection.commit()
    print("Book issued successfully!")

    connection.close()

def return_book():
    connection = get_db_connection()
    cursor = connection.cursor()

    transaction_id = int(input("Enter TransactionID to mark as returned: "))
    return_date = datetime.date.today()

    cursor.execute("UPDATE Transactions SET ReturnDate = %s WHERE TransactionID = %s", (return_date, transaction_id))
    connection.commit()

    cursor.execute("""
        SELECT BookID FROM Transactions WHERE TransactionID = %s
    """, (transaction_id,))
    book_id = cursor.fetchone()[0]

    cursor.execute("UPDATE Books SET Quantity = Quantity + 1 WHERE BookID = %s", (book_id,))
    connection.commit()

    print("Book returned successfully!")
    connection.close()
