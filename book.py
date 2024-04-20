#
#
#
#


class Book:
    # Initializer
    def __init__(self, i, t, a, g, avail):
        self.__isbn = i
        self.__title= t
        self.__author = a
        self.__g_code = g
        self.__available = avail

    # Method

    ## Borrow/Return
        # Borrow
    def borrow_it(self):
        self.__available = False
        if self.__available == False:
            return self.__available

        # Return
    def return_it(self):
        self.__available = True
        if self.__available == True:
            return self.__available
        
    ## Get
        # Get ISBN
    def get_isbn(self):
        return self.__isbn
    
        # Get Title
    def get_title(self):
        return self.__title
    
        # Get Author
    def get_author(self):
        return self.__author
    
        # Get Genre Name
    def get_genre_name(self):
        GENRE_LIST = ['Romance', 'Mystery', 'Science Fiction', 'Thriller', 'Young Adult', 'Children\'s Fiction',
                        'Self-help', 'Fantasy', 'Historical Fiction', 'Poetry']
        get = int(self.__g_code)
        genre = GENRE_LIST[get]
        return genre

        # Get Availability
    def get_availability(self):
        if self.__available == True:
            check = 'Available'
            return check
        else:
            check = 'Borrowed'
            return check
        
    ## Set
        # Set ISBN
    def set_isbn(self, isbn):
        self.__isbn = isbn

        # Set Title
    def set_title(self, title):
        self.__title = title

        # Set Author
    def set_author(self, author):
        self.__author = author

        # Set Genre
    def set_genre(self, g_code):
        self.__g_code = g_code

    ## Display
        # STR
    def __str__(self):
        #return f'{self.__isbn} {self.__title} {self.get_genre_name()}'
        return (f"{self.__isbn :<14} {self.__title :<25} {self.__author :<25} {self.get_genre_name() :<20} {self.get_availability()}")

    # Object
