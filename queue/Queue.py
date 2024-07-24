from ListNode import ListNode
#implementation of Queue: fifo dsa

class QueueArray(): #FIXED SIZE ARRAY IMPLEMENTATION
    def __init__(self, max_size):
        self.queue = [None]*max_size
        self.max_size = max_size
        self.size = 0
        self.head = 0
        self.tail = -1
    
    def __len__(self):
        return self.size
    
    def is_full(self):
        return True if len(self) == self.max_size else False

    def is_empty(self):
        return True if len(self) == 0 else False     
        
    
    def enqueue(self, value):
        if self.is_full() == True:
            raise IndexError("The queue is full")
        self.tail = (self.tail+1)%self.max_size
        self.queue[self.tail] = value
        self.tail = self.tail+1
        

    def dequeue(self):
        if self.is_empty() == True:
            raise IndexError("The queue is empty")
        removed = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head+1)%self.max_size
        self.head = self.head+1
        return removed

    def __str__(self):
        index = self.head
        str = ""
        if self.is_empty == True:
            raise IndexError("Queue is empty")
        for i in range(self.size):
            str = str(self.queue[index]) + "-->"
            index = (index + 1)%self.max_size
        return str
    
    def peek(self):
        if self.is_empty() == True:
            raise IndexError("The queue is empty")
        return self.queue[self.head]
    
class Queue(): #LINKED LIST IMPLEMENTATION
    def __init__(self, max_size):
        self.head = None #first element to be popped 
        self.tail = None #last element to be added
        self.size = 0
        self.max_size = max_size

    def __len__(self):
        return self.size

    def enqueue(self, value):
        node = ListNode(value)
        if self.is_full() == True:
            raise IndexError("The queue is full")
             
        else:
            self.size += 1

        if self.tail is None:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node
            self.tail = node
        
    def dequeue(self):
        if len(self) == 0:
            raise IndexError("The queue is empty")
        else:
            temp = self.head.value # save the pop element
            self.head = self.head.next # remove the first element in queue
            self.size -= 1
        return temp
    
    def is_empty(self):
        return True if len(self) == 0 else False
    
    def is_full(self):
        return True if len(self) == self.max_size else False
    
    def peek(self):
        if self.is_empty() == True:
            raise IndexError("The queue is empty")
        return self.head.value
    
    def __str__(self):
        arr = []
        cur = self.head
        while cur != None:
            arr.append(str(cur.value))
            cur = cur.next
        return "-->".join(arr)





    