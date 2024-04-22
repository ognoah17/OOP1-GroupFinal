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
    index = 0
    while index < len(books):
        current_book = books[index]
        #for each in current_book:
        isbn = current_book.get_isbn()
        title = current_book.get_title()
        author = current_book.get_author()
        genre = current_book.get_genre()
        available = current_book.get_availability()
        line = f'{isbn},{title},{author},{genre},{available}\n'
        fLines += line
        index += 1
    return fLines

# Load Books
def load_books(fileName):
    '''
    Takes and reads file name
    Converts lines to list
    Returns List
    '''
    books = []
    eachBook = []
    format = []
    with open(fileName, 'r') as file:
        for line in file:
            isbn, title, author, genre, availability = line.strip().split(',')
            format.append([isbn, title, author, genre, availability])
        for each in format:
            eachBook.append(Book(each[0],each[1],each[2],each[3],each[4]))
        for each in eachBook:
            books.append(each)
    return books

# Display Book
def print_single(books):
    if books == None:
        pass
    else:
        return print(books)

# Display Catalog
def print_books(books):
    '''
    --Print Book Catalog--
    '''
    print("Catalog of Books:")
    print("=" * 50)
    print("{:<15} {:<30} {:<20} {:<15} {:<10}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    for book in books:
        print_single(book)

##### 
'''
    << - Noah's Code - >>
'''
## - Should be Noah's
    # Add Book
def add_book(books):
    '''
    Add's a book to the catalog
    '''
    new_book = []
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    title = input('Enter title: ')
    author = input('Enter author name: ')
    g_valid = False
    while g_valid is False:
        genre = input('Enter genre: ')
        match genre:
            case 'Romance':
                genre = 0
                g_valid = True
            case 'Mystery':
                genre = 1
                g_valid = True
            case 'Science Fiction':
                genre = 2
                g_valid = True
            case 'Thriller':
                genre = 3
                g_valid = True
            case 'Young Adult':
                genre = 4
                g_valid = True
            case 'Children\'s Fiction':
                genre = 5
                g_valid = True
            case 'Self-help':
                genre = 6
                g_valid = True
            case 'Fantasy':
                genre = 7
                g_valid = True
            case 'Historical Fiction':
                genre = 8
                g_valid = True
            case 'Poetry':
                genre = 9
                g_valid = True
            case _:
                print('Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller,'
                        ' Young Adult, Children\'s Fiction, Self-help, Fantasy, Historical Fiction, Poetry')
    available = True
    new_book.append(Book(isbn, title, author, genre, available))
    for each in new_book:
        books.append(each)
    print(f'{title} with ISBN {isbn} successfully added')
    return books

    # Remove Book
def remove_book(books):
    '''
    Search for isbn
    If found, remove from books
    '''
    search = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    index = 0
    while index < len(books):
        current_book = books[index]
        if search in current_book.get_isbn():
            books.pop(index)
            print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} succesfully removed.")
            found = True
        else:
            index += 1
    if found == False:
        if index == len(books):
            print('No book found with that ISBN.')
#####

##### 
'''
    << - Rubal's Code - >>
'''
## - Should be Rubal's
    # Search Books
def search_books(books, search):
    '''
    Search for book
    Looks for match in:
    isbn, title, author, genre
    '''
    search_match = []
    index = 0
    while index < len(books):
        current_book = books[index]
        if search.lower() in current_book.get_title().lower():
            search_match.append(current_book)
        if search.lower() in (current_book.get_author().lower()):
            search_match.append(current_book)
        if search.lower() in (current_book.get_isbn().lower()):
            search_match.append(current_book)
        #if search.lower() in (current_book.get_genre().lower()):
            #search_match.append(current_book)
        index += 1
    print_books(search_match)

# Borrow Book
def borrow_book(books):
    '''
    Takes book list
    Search for isbn and finds match
    If available, sets as borrowed
    '''
    search = input(f'-- Borrow a book -- \nEnter the 13-digit ISBN (format 999-9999999999): ')
    index = 0
    while index < len(books):
        current_book = books[index]
        if search == current_book.get_isbn():
            if current_book.get_availability() == True:
                current_book.borrow_it()
                print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} successfully borrowed.")
                found = True
                break
            else:
                print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} is not currently available.")
                found == True
                break
        else:
            index += 1
    if found == False:
        if index == len(books):
            print('No book found with that ISBN')

# Return Book
def return_book(books):
    '''
    Takes book list
    Search for isbn and finds match
    If borrowed, sets as available
    '''
    search = input(f'-- Return a book -- \nEnter the 13-digit ISBN (format 999-9999999999): ')
    index = 0
    while index < len(books):
        current_book = books[index]
        if search == current_book.get_isbn():
            if current_book.get_availability() == False:
                current_book.return_it()
                print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} successfully returned.")
                break
            else:
                print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} is not currently borrowed.")
                break
        else:
            index += 1
    if index == len(books):
        print('No book found with that ISBN')
##### Borrow and Return do NOT use find_by_isbn function (function not made)
#####

# Menu
def menu(books, file_input):
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
                print('-- Search for books --')
                search = input('Enter search value: ')
                search_books(books, search)
            case '2': 
                # Borrow a book
                borrow_book(books)
            case '3':
                # Return a book
                return_book(books)
            case '0':
                # Exit the system
                format = format_books(books)
                exit_system(file_input, format)
                break

            # Librarian Menu
            case '2130':
                while True:
                    choice = print_libMenu()
                    match choice:
                        case '1':
                            # Search for books
                            print('-- Search for books --')
                            search = input('Enter search value: ')
                            search_books(books, search)
                        case '2': 
                            # Borrow a book
                            borrow_book(books)
                        case '3':
                            # Return a book
                            return_book(books)
                        case '4':
                            # Add a book
                            print('-- Add a book --')
                            add_book(books)
                        case '5':
                            # Remove a book
                            print('-- Remove a book --')
                            remove_book(books)
                        case '6':
                            # Print Catalog
                            load_books(file_input)
                            print_books(books)
                        case '0':
                            # Exit the system
                            format = format_books(books)
                            exit_system(file_input, format)
                            menu_loop = False
                            break
                        case '':
                            print('Invalid option')



# re Enter File
def reEnterFile():
    '''
    Let's the user re-input the file name if they type an incorrect name
    '''
    while True:
        file_input = input(f'File not found. Re-enter book catalog filename: ')
        if os.path.exists(file_input):
            books = []
            books = load_books(file_input)
            menu(books, file_input)

# Main
def main():
    '''
    Main
    '''
    print('Starting the system ...')
    file_input = input(f'Enter book catalog filename: ')
    if os.path.exists(file_input):
        books = []
        books = load_books(file_input)
        menu(books, file_input)
    else:reEnterFile()
                    
if __name__ == "__main__":
    menu_loop = True
    main()