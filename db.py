import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="sidonthetroll",  # Replace with your MySQL password
        database="LibraryDB"
    )

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            BookID INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(255),
            Author VARCHAR(255),
            Publisher VARCHAR(255),
            Quantity INT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Borrowers (
            BorrowerID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            Email VARCHAR(255),
            PhoneNumber VARCHAR(10)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            TransactionID INT AUTO_INCREMENT PRIMARY KEY,
            BookID INT,
            BorrowerID INT,
            IssueDate DATE,
            ReturnDate DATE,
            FOREIGN KEY (BookID) REFERENCES Books(BookID),
            FOREIGN KEY (BorrowerID) REFERENCES Borrowers(BorrowerID)
        )
    """)

    connection.commit()
    connection.close()
