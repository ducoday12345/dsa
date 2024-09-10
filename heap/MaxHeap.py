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
    
    def insert(self, value):
        self.heap.append(value)
        #heapify up for last value (newest value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, index): #heapify up
        parent_index = (index - 1)//2
        while index > 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def __str__(self):
        return str(self.heap)

    def sift_down(self, index): #heapify down needed for extract max
        size = self.get_size()
        while index < size:
            largest = index
            left_index = 2*index +1
            right_index = 2*index+2
            if left_index < size and self.heap[left_index] > self.heap[right_index]:
                largest = left_index
            if right_index < size and self.heap[right_index] > self.heap[left_index]:
                largest = right_index
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest
    def extract_max(self): #remove root node of max heap 
        pass
