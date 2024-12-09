from library_cli import add_book, view_books, edit_book, add_borrower, view_borrowers, edit_borrower, issue_book, return_book
from db import create_tables

def main_menu():
    print("""
    Library Management System
    1. Add Book
    2. View Books
    3. Edit Book
    4. Add Borrower
    5. View Borrowers
    6. Edit Borrower
    7. Issue Book
    8. Return Book
    9. Exit
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
            edit_book()
        elif choice == "4":
            add_borrower()
        elif choice == "5":
            view_borrowers()
        elif choice == "6":
            edit_borrower()
        elif choice == "7":
            issue_book()
        elif choice == "8":
            return_book()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
