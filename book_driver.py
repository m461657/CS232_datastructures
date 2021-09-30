import Book
import Library
import PriorityQueue

def add_to_library():

    title = input("What is the title of book?")
    author = input("Who is the author of the book?")
    year = input("What year was the book published?")

    while not year.isdigit():
        year = input("Re-enter the year as a number,\n'year' must be class int.")

    genre = input("What genre is the book?")

    book = Book.Book(str(title), str(author), int(year), str(genre))

    l.add_book(book)

    pq = input("Would you like to add this book to the Priority Queue? (yes/no)")
    if pq == "yes":
        add_to_pq(book)
    

def remove_from_library():
    print("removes")
    title = input("What is the title of the book you want to remove?")
    author = input("Who is the author of the book you want to remove?")

    l.remove_book(title, author)

    pq = input("Would you like to remove the highest priority book from the Priority Queue? (yes/no)")
    
    if pq == "yes":
        rem_pq()

def view_library():
    sort_l = input("Would you like to view a sorted Library? (yes/no)")
    if sort_l == "yes":
        l.sort()
    print(l)

    view_min = input("Would you like to view the highest priority book? (yes/no)")

    if view_min == "yes":
        view_min_pq()

    view_pq = input("Would you like to view the Priority Queue? (yes/no)")

    if view_pq == "yes":
        view_priorityq()

def add_to_pq(b):
    l.add_pq(b)

def rem_pq():
    l.remove_pq()

def view_min_pq():
    print(l.next_pq())

def view_priorityq():
    print(l.get_pq())


add = input("Would you like to create a new Library? (yes/no)")
if add == "yes":
    l = Library.Library()

while add == "yes":
    next_step = input("Would you like to add a book (add), remove a book (remove),\nview the library (view), or end the program (end)?")
    if next_step == "add":
        add_to_library()
        add = "yes"
    elif next_step == "remove":
        remove_from_library()
        add = "yes"
    elif next_step == "view":
        view_library()
        add = "yes"
    else:
        #re do this print statement later
        print("You elected to end the program,\nor entered unrecognizable input.")
        add = "no"


