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


if __name__ == "__main__":
    main()