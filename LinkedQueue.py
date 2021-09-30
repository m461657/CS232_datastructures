import Node

class LinkedQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def size(self):
        return(self.length)

    def is_empty(self):
        return(self.length == 0)

    def enqueue(self, item):
        temp = Node.Node(item)
        #print(temp)
        #self.front = temp
        if self.length == 0:
            #temp.set_next(self.front)
            #temp.set_next(self.rear)

            self.front = temp
            self.rear = temp
            #print(self.front)
            #print(self.rear)
        elif self.length >= 2:
            
            ## self.front needs to point to self.rear,
            ## self.rear needs to point to self.rear
            self.rear.set_next(temp)
            self.rear = temp
        else:
            self.front.set_next(temp)
            self.rear = temp
       # print(self.front)
        #print(self.front.get_next())
        #print(self.rear)
        self.length = self.length + 1

    def dequeue(self):   
        if self.front != None:
            temp = self.front.get_data()
            self.front = self.front.get_next()
            self.length = self.length - 1
        
            return(temp)
              
        else:
            return(None)
        
        
    def first(self):
        if self.front != None:
            temp = self.front.get_data()
            return(temp)
        else:
            return(None)

    def __str__(self):
        t = self.front
        queue = ""
        while t!= None:
            queue += str(t)
            queue += " "
            t = t.get_next()
            #self.front = self.front.get_next()
            
            #t = self.front
        if self.front == None:
            queue = ""
        #stack = stack[0:-2]
        return(str(queue))

        #change self.front