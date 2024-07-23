from ListNode import ListNode
#implementation of Queue: fifo dsa
class QueueArray():
    def __init__(self):
        self.queue_arr = []

class Queue(): #linked list implementation
    def __init__(self, max_size):
        self.head = None #first element to be popped 
        self.tail = None #last element to be added
        self.size = 0
        self.max_size = max_size

    def __len__(self):
        return self.size

    def enque(self, value):
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
        

    def deque(self):
        if len(self) == 0:
            raise IndexError("The queue is empty")
        else:
            temp = self.head.value # save the pop element
            self.head = self.head.next # remove the first element in queue
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





    