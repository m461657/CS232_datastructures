import Book
import Library

class PriorityQueue:

    def __init__(self):
        #initializes the PQ
        self.pq = []

    def insert(self, k):
        #appends item to the PQ
        self.pq.append(k)       
        #sorts the PQ with the new item in it
        if len(self.pq) >0:
            for i in range(len(self.pq) - 1, 0, -1):
                for j in range(i):
                    if self.pq[j] > self.pq[j + 1]:
                        temp = self.pq[j]
                        self.pq[j] = self.pq[j + 1]
                        self.pq[j + 1] = temp

    def get_min(self):
        #checks that PQ is not empty list
        #saves 0th item as a temp variable
        #returns temp (or None if list is empty)
        if self.pq != []:
            temp = self.pq[0]
            return(temp)
        return(None)
        
    def delete(self):
        #checks to see if len of list is greater than 0
        #saves 0th item as a temp variable
        #removes 0th item
        #returns temp variable
        if len(self.pq) >0:
            temp = self.pq[0]
            self.pq.pop(0)
            return(temp)
        return(None)

    def is_empty(self):
        #returns True if len is equal to 0, False if not
        if len(self.pq) == 0:
            return(True)
        return(False)

    def size(self):
        #returns the length (size)
        return(len(self.pq))

    