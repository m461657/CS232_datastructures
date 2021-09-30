import Node
#this will work like a regular stack but the underlying code is different
#the user DOES NOT CARE how the code is written/implemented
class LinkedStack:

    #only keep track of the top
    #uses nodes but isn't just a node

    def __init__(self):
        self.top = None
        self.length = 0

    def push(self,item):   #accepts an item but not a node
        #create a node using item as the data
        temp = Node.Node(item)
        #new top has to point to old top
        temp.set_next(self.top)
        #set new node to be the new top
        self.top = temp

    def peek(self):             #maybe convert to string then int? 
        if self.top != None:
            return(self.top.get_data())
        else:
            return(None)

    def pop(self):
        if self.top == None:
            return(None)
        top = self.top.get_data()
        self.top = self.top.get_next()
        return(top)

    def size(self):     #this works, when 3 items pushed, size = 3
        s = 0
        t = self.top
        #print(t)
        while t != None:
            s+= 1
            t = t.get_next()
        #print(self.length)
        self.length = s
        #return(self.length)
        return(self.length)

    def is_empty(self):
        if self.top == None:
            return(True)
        else:
            return(False)

    def __str__(self):
        t = self.top
        stack = ""
        while t!= None:
            stack += str(t)
            stack += " "
            t = t.get_next()
        if self.top == None:
            stack = ""
        #stack = stack[0:-2]
        return(str(stack))

