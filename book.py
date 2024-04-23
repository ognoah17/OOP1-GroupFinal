
class Book:

# get_genre_name()
    GENRE_NAMES = { 0:"Romance", 1:"Mystery", 2:"Science Friction", 3:"Thriller", 4:"Young Adult", 5:"Children's Fiction", 6:"Self-help", 7:"Fantasy", 8:"Historical Friction", 9:"Poetry"}
    def __init__(self, isbn, title, author, genre, available):
        self.isbn = isbn
        self.title =title
        self.author= author
        self.genre =genre
        self.available=available

        #implementing getters
         #get ISBN
        def get_isbn(self):
            return self.isbn
        #get TITLE
        def get_title(self):
            return self.title
        #get AUTHOR
        def get_author(self):
            return self.author
        #get GENRE
        def get_genre(self):
            return Book.GENRE_NAMES.get (self.genre, "Unknown")
        #get AVAILABLE
        def get_available(self):
            return "Available" if self.available else "Borrowed" 
       
        #Implementing Setters
        #Set ISBN
        def set_isbn(self,isbn):
            self.__isbn = isbn
        #set TITLE
        def set_title(self,title):
            self.__title= title
        #set AUTHOR
        def set_author(self,author):
            self.__author= author  
        #set GENRE
        def set_genre(self,genre):
            self.__genre= genre

        #RETURN
        def return_it(self):
            self.__availablr = True
        # BORROW
        def borrow_it(self):
            self.__available = False
        #__str__()
        def __str__(self):
            return "{:<14} {:<25} {:<20} {:<s}".format(self.__isbn, self.__title,self.__author,Book.GENRE_NAMES.get (self.genre, "Unknown"), "Available" if self.available else "Borrowed" )
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
    
        # Get Genre
    def get_genre(self):
        return self.__g_code
    
        # Get Genre Name
    def get_genre_name(self):
        GENRE_LIST = ['Romance', 'Mystery', 'Science Fiction', 'Thriller', 'Young Adult', 'Children\'s Fiction',
                        'Self-help', 'Fantasy', 'Historical Fiction', 'Poetry']
        get = int(self.__g_code)
        genre = GENRE_LIST[get]
        return genre

        # Get Availability
    def get_availability(self):
        if self.__available == 'True':
            return 'Available'
        else:
            return 'Borrowed'
        
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

        # Set Availability
    def set_availability(self):
        if self.__available == True:
            check = 'Available'
            return check
        else:
            check = 'Borrowed'
            return check

    ## Display
        # STR
    def __str__(self):
        #return f'{self.__isbn} {self.__title} {self.get_genre_name()}'
        return (f"{self.__isbn :<14} {self.__title :<25} {self.__author :<25} {self.get_genre_name() :<20} {self.get_availability()}")

    # Object
>>>>>>> main
