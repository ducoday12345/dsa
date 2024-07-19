from LinkedList import LinkedList

#initialize linked list: 7-->6-->5-->None
def initialize(head: LinkedList):
    head.push_front(5)
    head.push_front(6)
    head.push_front(7)
    print(f"Instantiate LL head: ")

def test_push_back(ll:LinkedList):
    head.push_back(69)
    print(f"Append '69' to end of LL: {ll}")  

def test_size(ll:LinkedList):
    print(f"Get length of LL: {len(ll)}")  

def test_empty(ll:LinkedList):
    print(f"Check if LL is empty: {ll.empty()}")  

def test_remove_at(ll:LinkedList):
    head.remove_at(2)
    print(f"Remove element at index 2: {ll}")  

def test_value_at(ll:LinkedList):
    print(f"Find value at index 2: {ll.value_at(2)}")  


if __name__ == "__main__":
    #initialize LL
    head = LinkedList()
    head_empty = LinkedList()

    #test function
    initialize(head)
    
    test_push_back(head)
    
    test_size(head)

    test_empty(head)
    test_empty(head_empty)

    test_remove_at(head)

    test_value_at(head)