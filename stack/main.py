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

if __name__ == "__main__":
    s = Stack()
    initialize(s)
    test_pop(s)
    test_peek(s)
