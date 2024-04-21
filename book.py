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