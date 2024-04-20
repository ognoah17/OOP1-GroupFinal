import os

def print_menu():
    '''
    Main Menu Screen
    User Input to select option
    '''
    print() # Empty line for readability
    print('Reader\'s Guild Library - Main Menu')
    print('='*34)
    print(f'1. Search for books \n2. Borrow \n3. Return a book \n4. Admin Menu \n0. Exit the system')
    userInput = input('Enter your selection: ')
    return userInput

def admin_menu():
    '''
    Admin Menu Screen
    User Input to select option
    '''
    print() # Empty line for readability
    print('Reader\'s Guild Library - Admin Menu')
    print('='*34)
    print(f'1. Add a book  \n2. Remove a book \n3. Print catalog \n0. Exit this menu')
    userInput = input('Enter your selection: ')
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
        print('Book catalog has been loaded.')
    return bookList

def main():
    '''
    Main
    '''
    print('Starting the system ...')
    fileInput = input(f'Enter book catalog filename: ')
    if os.path.exists(fileInput):
        books = load_books(fileInput)
    else:
        print('File not found. Exiting the system.')
        return

    while True:
        print('\nReader\'s Guild Library - Main Menu')
        print('='*34)
        print('1. Search for books')
        print('2. Borrow a book')
        print('3. Return a book')
        print('4. Admin Menu')
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
