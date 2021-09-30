class Book:

    def __init__(self, title, author, year, genre):
        #initializes class attributes
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre 

    def __eq__(self, other):
        #cchecks to see if author, title, and year are the same for self and other
        if self.title == other.get_title():
            if self.author == other.get_author():
                if self.year == other.get_year():
                    return(True)
        return(False)

    def __gt__(self, other):
        #checks if author is greater than that of other
        #if author is equal, checks to see if title is greater
        #continues on until all conditions are checked (or True is returned)
        #returns false if all attributes were equal or less than
        if self.author > other.get_author():
            return(True)
        if self.author == other.get_author():
            if self.title > other.get_title():  #this line doesn't work, idk why
                return(True)
        if self.title == other.get_title():
            if self.author == other.get_author():
                if self.year > other.get_year():
                    return(True)
        if self.title == other.get_title():
            if self.author == other.get_author():
                if self.year == other.get_year():
                    return(False)
        return(False)
    
    def __lt__(self, other):
        #does the same as __gt__ but checks for less than
        if self.author < other.get_author():
            return(True)
        if self.author == other.get_author():
            if self.title < other.get_title():
                return(True)
        if self.title == other.get_title():
            if self.author == other.get_author():
                if self.year < other.get_year():
                    return(True)
        if self.title == other.get_title():
            if self.author == other.get_author():
                if self.year == other.get_year():
                    if self.genre < other.get_genre():
                        return(False)
        return(False)


    def __ge__(self, other):
        #checks if equal and then if gt
        if self.__eq__(other):
            return(True)
        elif self.__gt__(other):
            return(True)
        else:
            return(False)

    def __le__(self, other):
        #checks if equal and then if lt
        if self.__eq__(other):
            return(True)
        elif self.__lt__(other):
            return(True)
        else:
            return(False)

    def get_title(self):
        #returns title
        return(self.title)

    def get_author(self):
        #returns author
        return(self.author)

    def get_year(self):
        #returns year
        return(self.year)
    
    def get_genre(self):
        #returns genre
        return(self.genre)

    def set_title(self, title):
        #sets title
        self.title = title

    def set_author(self, author):
        #sets author
        self.author = author

    def set_year(self, year):
        #sets year
        self.year = year

    def set_genre(self, genre):
        #sets genre
        self.genre = genre

    def __str__(self):
        #returns book object (attributes) as a string
        return(self.author + ', "' + self.title + '", ' + str(self.year) + ". " + self.genre + ".")