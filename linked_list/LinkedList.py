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
        pass
    
    #insert after index
    def insert(self,index,value):
        count = 0

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
            count += 1
            cur = cur.next

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

    #print linked list
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