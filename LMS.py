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

# Exit System
def exitSystem():
    '''
    Saves changes to the catalog
    Displays exit message
    Exits Main loop
    '''

# Format Books
def format_books(books):
    '''
    Gets list of books
    Formats book data
    '''
    fLines = ''
    for each in books:
        line = f'{each[0]},{each[1]},{each[2]},{each[3]},{each[4]}\n'
        fLines += line
    return fLines

# Load Books
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

# Main
def main():
    '''
    Main
    '''
    print('Starting the system ...')
    fileInput = input(f'Enter book catalog filename: ')
    if os.path.exists(fileInput):
        books = []
        books = load_books(fileInput)
    print('Book catalog has been loaded.')

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
                            # Add a book
                            print('Add a book -- goes here')
                        case '5':
                            # Remove a book
                            print('Remove a book -- goes here')
                        case '6':
                            # Print Catalog
                            print('Print catalog -- goes here')
                        case '0':
                            # Exit the system
                            format = format_books(books)
            


if __name__ == "__main__":
    main()