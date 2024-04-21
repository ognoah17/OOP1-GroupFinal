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
def exit_system(fileName, fLines):
    '''
    Saves changes to the catalog
    Displays exit message
    Exits Main loop
    '''
    with open(fileName,'w') as file:
        file.write(fLines)
    print(f'-- Exit the system -- \nBook catalog has been saved. \nGood Bye!')

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

def print_books(books):
    '''
    --Print Book Catalog--
    '''
    print("Catalog of Books:")
    print("=" * 50)
    print("{:<15} {:<30} {:<20} {:<15} {:<10}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    for book in books:
        isbn, title, author, genre, availability = book
        print("{:<15} {:<30} {:<20} {:<15} {:<10}".format(isbn, title, author, genre, availability))

def menu(books):
    '''
    Menu options
    '''
    print('Book catalog has been loaded.')
    global menu_loop
    while menu_loop == True:
        choice = print_menu()

            # Main Menu
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
                #format = format_books(books)
                #exit_system(fileInput, format)
                break

            # Librarian Menu
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
                            print_books(books)
                        case '0':
                            # Exit the system
                            #format = format_books(books)
                            #exit_system(fileInput, format)
                            menu_loop = False
                            break

def reEnterFile():
    '''
    Let's the user re-input the file name if they type an incorrect name
    '''
    while True:
        fileInput = input(f'File not found. Re-enter book catalog filename: ')
        if os.path.exists(fileInput):
            books = []
            books = load_books(fileInput)
            menu(books)
            return fileInput
    


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
        menu(books)
        return fileInput
    else:reEnterFile()
                    
if __name__ == "__main__":
    menu_loop = True
    main()