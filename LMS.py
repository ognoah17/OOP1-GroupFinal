
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


# Print Menu        ------------------------------------------> GOOD
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
    
# Print Librarian Menu  -------------------------------------> GOOD
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

# Exit System           ------------------------------------> GOOD
def exit_system(fileName, fLines):
    '''
    Saves changes to the catalog
    Displays exit message
    Exits Main loop
    '''
    with open(fileName,'w') as file:
        file.write(fLines)
    print(f'-- Exit the system -- \nBook catalog has been saved. \nGood Bye!')

# Format Books ----------------------- << Testing Required >>
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

# Load Books <<<<<<<<<<<<<<<< GOOD (- availability?)
def load_books(filename):
    books = []
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) != 5:
                    print(f"Error on line {line_number}: expected 5 values, got {len(parts)}. Line content: '{line}'")
                    continue  # Skip this line
                isbn, title, author, genre, availability = parts
                books.append({'isbn': isbn.strip(), 'title': title.strip(), 'author': author.strip(), 'genre': genre.strip(), 'availability': availability.strip()})
    return books


# Display Book      -------------------------------------> GOOD
def print_single(books):
    if books == None:
        pass
    else:
        return print(books)

# Display Catalog   -------------------------------------> GOOD
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
def add_book(fileName, book_list):
    print('--Add a Book--')
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    title = input('Enter title: ')
    author = input('Enter author name: ')
    
    # Display available genres with codes
    print("Enter genres:")
    genre_list = [
        'Romance', 'Mystery', 'Science Fiction', 'Thriller', 
        'Young Adult', "Children's Fiction", 'Self-help', 
        'Fantasy', 'Historical Fiction', 'Poetry'
    ]
    for i, genre in enumerate(genre_list):
        print(f"{i}: {genre}")
    
    # Prompt the user to select a genre code
    genre_code = int(input('Enter genre code (0-9): '))
    while genre_code not in range(10):
        print('Invalid genre. Choice are as above:')
        genre_code = int(input('Enter genre code (0-9): '))
    
    genre = genre_list[genre_code]
    
    availability =  'True'
    
    # Create a Book object
    new_book = Book(isbn, title, author, genre_code, availability)  # Use genre_code instead of genre
    
    # Append the new book to the book list
    book_list.append(new_book)
    
    # Append the new book entry to the file
    new_book_entry = f"{isbn},{title},{author},{genre_code},{availability}\n"
    with open(fileName, 'a') as file:
        file.write(new_book_entry)
    
    print(f'\'{title}\' with ISBN {isbn} successfully added.')

#####

##### 
'''
    << - Rubal's Code - >>
'''
#To search about books
def search_books(search_string, books):
    '''
    Searches for books based on the search string provided by the user.
    Returns a list of books matching the search criteria.
    '''
    search_result = []

    # Convert search string to lowercase for case-insensitive matching
    search_string = search_string.lower()

    for book in books:
        # Convert book attributes to lowercase for case-insensitive matching
        isbn = book['isbn'].lower()
        title = book['title'].lower()
        author = book['author'].lower()
        genre = book['genre'].lower()

        # Check if the search string appears in isbn, title, author, or genre
        if search_string in isbn or search_string in title or search_string in author or search_string in genre:
            search_result.append(book)

    return search_result





#To borrow a book
def borrow_book(books):
    '''
    Allow user to borrow the book
    '''
    isbn= input("Enter the 13-digit ISBN (format 999-99999999):")
    index = find_book_by_isbn(books,isbn)
    if index is not None:
        if books[index][4] =="Available":
            books[index][4] ="Borrowed"
            print(f" '{books[index][1]}' with ISBN {books[index][0]} successfully borrowed.")
        else:
            print(f" '{books[index][1]}' with ISBN {books[index][0]} is not currently available.")
    else:
        print("No book found with that ISBN.")

#Return book 
def return_book(books):
    '''
    Allow user to Return book
    '''
    isbn= input("Enter the 13-digit ISBN(format 999-99999999):")
    index= find_book_by_isbn(books,isbn)
    if index != -1:
        if books[index][4]== "Borrowed":
            books[index][4] ="Available"
            print(f"'{books[index][1]}' with ISBN {books[index][0]} successfully returned.")
        else:
            print(f"'{books[index][1]}' with ISBN {books[index][0]} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")

#Find book bt ISBN
def find_book_by_isbn(books, isbn):
    '''
    Finds book by ISBN
    '''
    index=0
    for book in books:
        if book[0] == isbn:
            return index
    return -1
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
                search_term = input("Enter the search term: ")
                result = search_books(search_term, books)
                print_books(result) 
            case '2': 
                # Borrow a book
                print('Borrow a book -- Goes here')
            case '3':
                # Return a book
                print('Return a book -- Goes here')
            case '0':
                # Exit the system
                #format = format_books(books)
                #exit_system(file_input, format)
                break

            # Librarian Menu
            case '2130':
                while True:
                    choice = print_libMenu()
                    match choice:
                        case '1':
                            search_term = input("Enter the search term: ")
                            result = search_books(search_term, books)
                            print_books(result) 
                        case '2': 
                            # Borrow a book
                            print('Borrow a book -- Goes here(same as other)')
                        case '3':
                            # Return a book
                            print('Return a book -- Goes here(same as other)')
                        case '4':
                            add_book(file_input, books)
                        case '5':
                            # Remove a book
                            print('Remove a book -- goes here')
                        case '6':
                            # Print Catalog
                            load_books(file_input)
                            print_books(books)
                        case '0':
                            # Exit the system
                            #format = format_books(books)
                            #exit_system(file_input, format)
                            menu_loop = False
                            break



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
    menu_loop= True
    main()