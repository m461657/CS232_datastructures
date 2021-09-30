import LinkedQueue
import Node

class LinkedDeque(LinkedQueue.LinkedQueue):

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def add_front(self, item):
        #add a node to front of queue
        temp = Node.Node(item)
    
        if self.length == 0:
            
            self.front = temp
            self.rear = temp
           
        elif self.length >= 2:
            #temp is pointing to self.front (T)-->self.front-->
            temp.set_next(self.front)
            #save temp as new self.front  (T=self.front)-->old front-->
            self.front = temp
        else:
            f = self.front
            temp.set_next(self.front)
            self.rear = f
            self.front = temp


        self.length = self.length +1

    def add_rear(self, item):
        super().enqueue(item)

    def remove_front(self):
        #remove and return item at the front of the queue
        return(super().dequeue())

    def remove_rear(self):
        #remove and return the item at the rear of the queue
        if self.rear != None:
            f = self.front
            r = self.rear
            current_rear = self.rear
            new_rear = None
            while f != r:
                if f.get_next() == r:
                    break
                else:
                    f=f.get_next()
        
            self.rear = f
            temp = current_rear.get_data()
            self.length = self.length - 1
            return(temp)
              
        else:
            return(None)

    def get_front(self):
        #return but don't remove item at front
        return(super().first())

    def get_rear(self):
        #return but don't remove item at the rear
        if self.rear!= None:
            temp = self.rear.get_data()
            return(temp)

        else:
            return(None)

    def size(self):
        return(super().size())

    def is_empty(self):
        return(self.length==0)

    def __str__(self):
        return(super().__str__())