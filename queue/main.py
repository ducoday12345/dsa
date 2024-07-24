from Queue import QueueArray, Queue

class TestLLQueue:

    def initialize(queue: Queue):
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(6)
        queue.enqueue(1)
        print(f"Create initial queue: {queue}")

    def test_pop(queue:Queue):
        print(f"POP! The removed value {queue.dequeue()}") 
        print(f"New Queue: {queue}") 

    def test_peek(queue:Queue):
        print(f"Top of the queue value: {queue.peek()}") 

    def is_full(queue:Queue):
        print(f"Check if queue is full: {queue.is_full()}") 

    def test_llqueue(self,queue:Queue):
        self.initialize(queue)
        self.is_full(queue)
        self.test_pop(queue)
        self.test_peek(queue)

class TestArrQueue:
    def initialize(queue: QueueArray):
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(6)
        queue.enqueue(1)
        queue.enqueue(7)
        print(f"Create initial queue: {queue}")

    def test_pop(queue:QueueArray):
        print(f"POP! The removed value {queue.dequeue()}") 
        print(f"New Queue: {queue}") 

    def test_peek(queue:QueueArray):
        print(f"Top of the queue value: {queue.peek()}") 

    def is_full(queue:QueueArray):
        print(f"Check if queue is full: {queue.is_full()}") 

    def test_llqueue(self,queue:QueueArray):
        self.initialize(queue)
        self.is_full(queue)
        self.test_pop(queue)
        self.test_peek(queue)


if __name__ == "__main__":
    s = Queue(5)
    ss = Queue(5)
    # TestLLQueue.initialize(s)
    # TestLLQueue.is_full(s)
    # TestLLQueue.test_pop(s)
    # TestLLQueue.test_peek(s)

    TestArrQueue.initialize(ss)
    TestArrQueue.is_full(ss)
    TestArrQueue.test_pop(ss)
    TestArrQueue.test_peek(ss)
