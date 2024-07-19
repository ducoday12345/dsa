'''
This is an implementation of a singly linked list
'''

from ListNode import ListNode

class LinkedList:
    def __init__(self):
        self.head = None

    #append value to front of linked list
    def push_front(self, value): 
        node = ListNode(value, self.head)
        self.head = node

    # append value to the end of linked list 
    def push_back(self,value): 
        node = ListNode(value, None)
        if self.head == None:
            self.next = node
            return
        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        return
    
    #pop first element
    def pop_front(self):
        if len(self) == 0:
            raise IndexError("The linked list is empty.")
        self.head =self.head.next

    #pop first element
    def pop_back(self):
        cur = self.head
        count = 0
        if len(self) == 0:
            raise IndexError("The linked list is empty.")
        while cur.next != 0:
            if count == len(self)  - 2:
                cur.next = None
                break
            cur = cur.next
            count += 1

    #get first value
    def front(self):
        return self.head.value
    
    #get last value
    def back(self):
        if len(self) == 0:
            raise IndexError("The linked list is empty.")
        cur = self.head
        while cur.next!= None:
            cur = cur.next
        return cur.value
        


    #insert after index
    def insert(self, value , index = 0):
        count = 0
        cur = self.head
        
        if index < 0 or index>len(self):
            raise Exception("Invalid index")
        if index == 0:
            self.push_front(value)
        while cur != None:
            if count == index - 1:
                node = ListNode(value, cur.next)
                cur.next = node
                break
            cur = cur.next
            count += 1


    #remove value at index
    def remove_at(self, index):
        count = 0

        if index < 0 or index >= len(self):
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return

        cur = self.head
        while cur != None:
            if count == index-1:
                cur.next = cur.next.next
                break
            cur = cur.next
            count += 1

    #find value at index
    def value_at(self, index):
        count = 0
        if count < 0 or count >= len(self):
            raise Exception("Invalid Index")
        cur = self.head
        while cur != None:
            if count == index:
                return cur.value
            count += 1
            cur = cur.next

    #Print linked list
    def __str__(self):
        if self.head == None:
            print("Linked list is empty")
            return
        
        cur = self.head
        string = ""
        
        while cur != None:
            string += str(cur.value) + "-->"
            cur = cur.next
        string += "None" # for end of the linked list
        
        return(string)
    
    #get length of linked list
    def __len__(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    #check empty
    def empty(self):
        return True if len(self) == 0 else False
    
    #Reverse LL
    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev
        return prev
    
    #removes the first item in the list with this value
    def remove_value(self,value):
        if len(self) == 0:
            raise IndexError("The linked list is empty.")
        
        # If the value is in the head node
        if self.head.value == value:
            self.head = self.head.next
        cur = self.head

        # Traverse the list to find the value
        while cur!= None:
            if cur.next.value == value:
                cur.next = cur.next.next
                return
            cur = cur.next
        raise ValueError(f"Value {value} not found in the LL")
        