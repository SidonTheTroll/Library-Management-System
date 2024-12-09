from library_cli import add_book, view_books, add_borrower, view_borrowers, issue_book, return_book
from db import create_tables

def main_menu():
    print("""
    Library Management System
    1. Add Book
    2. View Books
    3. Add Borrower
    4. View Borrowers
    5. Issue Book
    6. Return Book
    7. Exit
    """)

def main():
    create_tables()  # Ensure tables exist
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            add_borrower()
        elif choice == "4":
            view_borrowers()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
