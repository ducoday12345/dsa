from LinkedList import LinkedList

#initialize linked list: 7-->6-->5-->None
def initialize(ll: LinkedList):
    ll.push_front(5)
    ll.push_front(6)
    ll.push_front(7)
    print(f"Create initial LL: ")

def test_push_front(ll:LinkedList):
    new_value = 13
    ll.push_front(new_value)
    print(f"Append '{new_value}' to beginning of LL: {ll}")  

def test_push_back(ll:LinkedList):
    new_value = 69
    ll.push_back(new_value)
    print(f"Append '{new_value}' to end of LL: {ll}")  

def test_size(ll:LinkedList):
    print(f"Get length of LL: {len(ll)}")  

def test_empty(ll:LinkedList):
    print(f"Check if LL is empty: {ll.empty()}")  

def test_remove_at(ll:LinkedList):
    index = 2
    ll.remove_at(index)
    print(f"Remove element at index {index}: {ll}")  

def test_value_at(ll:LinkedList):
    index = 2
    print(f"Find value at index {index}: {ll.value_at(index)}") 

def test_insert(ll:LinkedList):
    index = 3
    value = 123
    ll.insert(value,index)
    print(f"Insert value {value} at index {index}: {ll}")

def test_pop_front(ll:LinkedList):
    ll.pop_front()
    print(f"Remove the first element of LL we have new LL: {ll}")  

def test_pop_back(ll:LinkedList):
    ll.pop_back()
    print(f"Remove the last element of LL we have new LL: {ll}") 

def test_front(ll:LinkedList):
    print(f"Get the first value of LL: {ll.front()}")

def test_back(ll:LinkedList):
    print(f"Get the last value of LL: {ll.back()}")

def test_reverse(ll:LinkedList):
    ll.reverse()
    print(f"Reverse of the current LL is: {ll}")

def test_remove_value(ll:LinkedList):
    value = 5
    ll.remove_value(value)
    print(f"Removes the first item in the list with this value '{value}': {ll}")


if __name__ == "__main__":
    #initialize LL
    head = LinkedList()
    head_empty = LinkedList()

    #test function
    initialize(head)
    test_push_front(head)
    test_push_back(head)
    test_size(head)
    test_empty(head)
    test_empty(head_empty)
    test_remove_at(head)
    test_value_at(head)
    test_insert(head)
    test_pop_front(head)
    test_pop_back(head)
    test_front(head)
    test_back(head)
    test_reverse(head)
    test_remove_value(head)