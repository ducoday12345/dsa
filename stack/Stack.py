from ListNode import ListNode
#LIFO type of data structure


class Stack:    #implementation using linked list
    def __init__(self):
        self.head = None # last element of the stack => first one to remove if pop()
        self.tail = None #first element of the stack => last one to remove if pop()
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False
        
    def push(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def pop(self):
        if self.is_empty() == True:
            raise IndexError("Stack is empty")
        temp = self.head #save head of the stack to temp 
        self.head = self.head.next
        if self.head.next == None:
            self.tail = None

        return temp.value # return the removed value
    
    def peek(self): #return the value at top of the stack
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.value


    def __str__(self):
        stack = []
        cur = self.head
        while cur != None:
            stack.append(str(cur.value))
            cur = cur.next
        return "-->".join(stack)