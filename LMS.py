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
    print(f'1. Search for books \n2. Borrow \n3. Return a book \n0. Exit the system')
    userInput = input('Enter you selection: ')
    return userInput
    
    

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
            print('Book catalog has been loaded.')
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
        print('\nReader\'s Guild Library - Main Menu')
        print('='*34)
        print('1. Search for books')
        print('2. Borrow a book')
        print('3. Return a book')
        print('0. Exit the system')
        choice = input('Enter your selection: ')

        if choice == '1':
            # Search for books
            print('Search for books -- Goes here')
        elif choice == '2':
            # Borrow a book
            print('Borrow a book -- Goes here')
        elif choice == '3':
            # Return a book
            print('Return a book -- Goes here')
        elif choice == '2130':
            # Admin Menu
            while True:
                print('\nReader\'s Guild Library - Admin Menu')
                print('='*34)
                print('1. Search for books')
                print('2. Borrow a book')
                print('3. Return a book')
                print('4. Add a book')
                print('5. Remove a book')
                print('6. Print catalog')
                print('0. Exit to main menu')
                admin_choice = input('Enter your selection: ')
                
                if admin_choice == '1':
                    # Add a book
                    print('Add a book -- Goes here')
                elif admin_choice == '2':
                    # Remove a book
                    print('Remove a book -- Goes here')
                elif admin_choice == '3':
                    # Print catalog
                    print('Print catalog -- Goes here')
                elif admin_choice == '0':
                    # Exit admin menu
                    break
                else:
                    print('Invalid choice. Please try again.')
        elif choice == '0':
            print('Exiting the system...')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()