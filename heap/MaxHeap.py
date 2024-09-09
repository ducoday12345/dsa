class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def get_size(self):
        return len(self.heap)
    
    def is_empty(self):
        return self.get_size == 0

    def get_max(self):
        if not self.is_empty():
            return self.heap[0]
        return None
    
    