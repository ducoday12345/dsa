from Queue import Queue

def initialize(queue: Queue):
    queue.enque(3)
    queue.enque(5)
    queue.enque(6)
    queue.enque(1)
    print(f"Create initial queue: {queue}")

def test_pop(queue:Queue):
    print(f"POP! The removed value {queue.deque()}") 
    print(f"New Queue: {queue}") 

def test_peek(queue:Queue):
    print(f"Top of the queue value: {queue.peek()}") 

def is_full(queue:Queue):
    print(f"Check if queue is full: {queue.is_full()}") 

if __name__ == "__main__":
    s = Queue(4)
    initialize(s)
    is_full(s)
    test_pop(s)
    test_peek(s)
