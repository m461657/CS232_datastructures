import Book
import PriorityQueue

class Library():

    def __init__(self):
        #initializes books list (Library) and PQ using PQ class     
        self.books = []
        self.pq = PriorityQueue.PriorityQueue()

    def set_books(self, books):
        #sets class attribute self.books
        self.books = books

    def get_books(self):
        #returns Library object
        return(self.books)

    def add_book(self, b):
        #saves the input b as a book object by calling book functions to get the title, author etc.PriorityQueue
        #appends book object to the Library
        book = Book.Book(b.get_title(), b.get_author(), b.get_year(), b.get_genre())
        self.books.append(book)

    def remove_book(self, title, author):
        #checks to see if self.books is empty
        #loops through books in self.books
        #if the title and author of the book in position i equals
        #the given title and author, the book is removed and returned
        #else, returns None
        if self.books != None:
            for book in self.books:
                if book.get_title() == title and book.get_author() == author:
                    temp = book
                    self.books.remove(temp)
                    return(book)
        return(None)

    def sort(self):
        #sort function from the textbook (bubble sort)
        for i in range(len(self.books) - 1, 0, -1):
            for j in range(i):
                if self.books[j] > self.books[j + 1]:
                    temp = self.books[j]
                    self.books[j] = self.books[j + 1]
                    self.books[j + 1] = temp

    def __str__(self):
        #initializes an empty string
        #loops through books, anf pulls the attributes from the book object in the Library
        #adds those objects to the string with formatting (includes newline)
        #returns string of books in self.books
        string = ""
        for book in self.books:
            #reconvert as a book object
            title = book.get_title()
            author = book.get_author()
            year = book.get_year()
            genre = book.get_genre()

            string += str(author) + ', "' + str(title) + '", ' + str(year) + ". " + str(genre) + ".\n"
            string = str(string)
        return(string)

    def get_pq(self):
        #returns self,pq if it isn't None
        if self.pq != None:
            return(self.pq)
        return(None)

    def add_pq(self, b):
        #inserts book object to PQ, calling insert (a PQ function)
        book = Book.Book(b.get_title(), b.get_author(), b.get_year(), b.get_genre())
        self.pq.insert(book)
        #self.pq.sort()

    def remove_pq(self):
        #if PQ is not empty, calls delete() from PQ class
        #saves the book being deleted as a temp to return
        if self.pq != None:
            temp = self.pq.delete()
            return(temp)
        return(None)

    def next_pq(self):
        #returns the results of calling get_min on the PQ
        return(self.pq.get_min())
        
    
    