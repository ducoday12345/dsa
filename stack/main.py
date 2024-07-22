from Stack import Stack

def initialize(stack: Stack):
    stack.push(3)
    stack.push(5)
    stack.push(6)
    stack.push(1)
    print(f"Create initial stack: {stack}")

def test_pop(stack:Stack):
    print(f"POP! The removed value {stack.pop()}") 
    print(f"New stack: {stack}") 

def test_peek(stack:Stack):
    print(f"Top of the stack value: {stack.peek()}") 

def is_full(stack:Stack):
    print(f"Check if stack is full: {stack.is_full()}") 

if __name__ == "__main__":
    s = Stack(4)
    initialize(s)
    is_full(s)
    test_pop(s)
    test_peek(s)
