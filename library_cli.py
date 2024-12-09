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

    cursor.execute("INSERT INTO Books (Title, Author, Publisher, Quantity) VALUES (%s, %s, %s, %s)", 
                   (title, author, publisher, quantity))
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

def add_borrower():
    connection = get_db_connection()
    cursor = connection.cursor()

    name = input("Enter borrower's name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    cursor.execute("INSERT INTO Borrowers (Name, Email, PhoneNumber) VALUES (%s, %s, %s)", 
                   (name, email, phone))
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
