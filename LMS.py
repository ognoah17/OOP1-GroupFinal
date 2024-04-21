#To search about books
def search_books(books, search_str):
    search_results= []
    for book in books:
        if search_str.lower() in [item.lower() for item in book]:
            search_results.append(book)
    return search_results


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