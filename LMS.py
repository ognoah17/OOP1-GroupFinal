#
# Library Management System
# Steven, Rubal, Noah
# April 20, 2024
#
# Imports book data from separate file
# ###user has the option to view or edit data in the file
# ###user can also calculate the average gpa of the students
#

import os
from book import Book

# Print Menu
def print_menu():
    '''
    Main Menu Screen
    User Input to select option
    '''
    print() # Empty line for readability
    print('Reader\'s Guild Library - Main Menu')
    print('='*34)
    print(f'1. Search for books \n2. Borrow a book \n3. Return a book \n0. Exit the system')
    userInput = input('Enter you selection: ')
    return userInput
    
# Print Librarian Menu
def print_libMenu():
    '''
    Librarian Menu Screen
    User Input to select option
    '''
    print() # Empty line for readability
    print('Reader\'s Guild Library - Librarian Menu')
    print('='*39)
    print(f'1. Search for books \n2. Borrow a book \n3. Return a book \n4. Add a book \n5. Remove a book \n6. Print catalog \n0. Exit the system')
    userInput = input('Enter you selection: ')
    return userInput

def load_books(fileName):
    '''
    Takes and reads file name
    Converts lines to list
    Returns List
    '''
    bookList = []
    with open(fileName, 'r') as file:
        for line in file:
            isbn, title, author, genre, availability = line.strip().split(',')
            bookList.append([isbn, title, author, genre, availability])
    return bookList

def print_books(books):
    '''
    Prints the catalog of books
    '''
    print("Catalog of Books:")
    print("=" * 50)
    print("{:<15} {:<30} {:<20} {:<15} {:<10}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    for book in books:
        isbn, title, author, genre, availability = book
        print("{:<15} {:<30} {:<20} {:<15} {:<10}".format(isbn, title, author, genre, availability))

def main():
    '''
    Main
    '''
print('Starting the system ...')
while True:
    file_input = input('Enter book catalog filename: ')
    if os.path.exists(file_input):
        books = load_books(file_input)
        print('Book catalog has been loaded.')
        break  # Exit the loop if the file exists and is loaded successfully
    else:
        print('Error: Book catalog file does not exist. Please re-enter.')

while True:
    choice = print_menu()
    match choice:
        case '1':
            # Search for books
            print('Search for books -- Goes here')
        case '2': 
            # Borrow a book
            print('Borrow a book -- Goes here')
        case '3':
            # Return a book
            print('Return a book -- Goes here')
        case '0':
            # Exit the system
            print('Exit the system -- Goes here')
        case '2130':
            while True:
                choice = print_libMenu()
                match choice:
                    case '1':
                        # Search for books
                        print('Search for books -- Goes here(same as other)')
                    case '2': 
                        # Borrow a book
                        print('Borrow a book -- Goes here(same as other)')
                    case '3':
                        # Return a book
                        print('Return a book -- Goes here(same as other)')
                    case '4':
                        add_book(file_input)
                    case '5':
                        # Remove a book
                        remove_book(file_input)
                    case '6':
                        # Print Catalog
                        print_books(books)  # Call the print_books function to display the catalog
                    case '0':
                        # Exit the system
                        print('Exit the system -- Goes here(same as other)')
        


if __name__ == "__main__":
    main()