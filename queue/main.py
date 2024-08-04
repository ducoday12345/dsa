from Queue import QueueArray, Queue, DeQue

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
        
class TestDeQue:
    def initialize(queue: DeQue):
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(6)
        queue.enqueue(1)
        print(f"Create initial queue: {queue}")

    def test_pop(queue:DeQue):
        print(f"POP! The removed value {queue.dequeue()}") 
        print(f"New Queue: {queue}") 

    def test_peek(queue:DeQue):
        print(f"Top of the queue value: {queue.peek()}") 

    def is_full(queue:DeQue):
        print(f"Check if queue is full: {queue.is_full()}") 

    def test_llqueue(self,queue:DeQue):
        self.initialize(queue)
        self.is_full(queue)
        self.test_pop(queue)
        self.test_peek(queue)


if __name__ == "__main__":
    t0 = Queue(5)
    t1 = Queue(5)
    t2 = DeQue(5)
    TestLLQueue.initialize(t0)
    TestLLQueue.is_full(t0)
    TestLLQueue.test_pop(t0)
    TestLLQueue.test_peek(t0)

    TestArrQueue.initialize(t1)
    TestArrQueue.is_full(t1)
    TestArrQueue.test_pop(t1)
    TestArrQueue.test_peek(t1)
    
    TestArrQueue.initialize(t2)
    TestArrQueue.is_full(t2)
    TestArrQueue.test_pop(t2)
    TestArrQueue.test_peek(t2)
