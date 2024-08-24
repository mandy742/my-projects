import sqlite3
import os
# Creating full path to the database file.
db_path = os.path.join('data', 'ebookstore.db')

try:
    # Create or connect to the database
    # TRy and expect to handle connection errors
    db = sqlite3.connect('db_path')
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    exit()
cursor = db.cursor()

# Create the 'book' table if it doesn't exist.
# If the table exists or created it must include the id, title, author and quantity.
cursor.execute('''
    CREATE TABLE IF NOT  EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
''')

# Populate the table with the provided data
books_data = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

cursor.executemany('INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', books_data)
db.commit()

# User selects an option they prefer from the menu.
# User must choose to enter,update,delete,search a book or exit.
while True:
    print('\nMenu:')
    print('1. Enter book')
    print('2. Update book')
    print('3. Delete book')
    print('4. Search books')
    print('0. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        # Add a new book
        title = input('Enter book title: ')
        book_id = int(input('Enter the book_id: '))
        author = input('Enter author: ')
        qty = int(input('Enter quantity: '))
        # Check lf a book with same id exists
        cursor.execute('SELECT id FROM book WHERE id = ?', (book_id,))
        existing_book = cursor.fetchone()
        if existing_book:
            print(f"Book with ID{book_id} already exists. Please choose a different ID")
        else:
            cursor.execute('INSERT INTO book (title, author, qty) VALUES (?, ?, ?)', (title, author, qty))
            db.commit()
            print('Book added successfully!')

    elif choice == '2':
        # Update book information
        # User must choose to update the title, author or quantity of the books.
        book_id = int(input('Enter book ID to update: '))
        print('Select field to update: ')
        print('1. Title')
        print('2. Author')
        print('3. Quantity')
        select_option = input('Enter your choice: ')

        if select_option == '1':
            # Update book title
            new_title = input('Enter new title: ')
            cursor.execute('UPDATE book SET title = ? WHERE id = ?', (new_title, book_id))
            db.commit()
            print('Book title updated!')

        elif select_option == '2':
            # Update book author
            new_author = input('Enter new author: ')
            cursor.execute('UPDATE book SET author = ? WHERE id = ?', (new_author, book_id))
            db.commit()
            print('Book author updated!')

        elif select_option == '3':
            # Update book quantity
            new_qty = int(input('Enter new quantity: '))
            cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (new_qty, book_id))
            db.commit()
            print('Book quantity updated!')

        else:
            print("Invalid choice. Please select a valid option.")

            db.commit()
            print('Book information updated!')

    elif choice == '3':
        # Delete a book
        book_id = int(input('Enter book ID to delete: '))
        cursor.execute('DELETE FROM book WHERE id = ?', (book_id,))
        db.commit()
        print('Book deleted successfully!')

    elif choice == '4':
        # Search for a book
        search_term = input('Enter search term (title or author): ')
        cursor.execute('SELECT * FROM book WHERE title LIKE ? OR author LIKE ?',
                       ('%' + search_term + '%', '%' + search_term + '%'))
        # Fetching all the books.
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f'ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Quantity: {row[3]}')
        else:
            print('No matching books found.')

    elif choice == '0':
        # Exit the program
        break

    else:
        print("Invalid choice. Please select a valid option.")

# close and save changes
db.commit()
db.close()
print('Connection to database closed')
