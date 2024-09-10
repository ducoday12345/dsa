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
        if self.is_empty() == True:
            return None
        if self.get_size() == 1:
            return self.heap.pop()
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return max_item

    def remove(self, index): #remove node of heap
        if index < 0 and index >= self.get_size():
            raise Exception("Index out of bound")
        self.heap[index] = self.heap.pop()
        if index > 0 and self.heap[index] > self.heap[(index-1)//2]:
            self.sift_up(index)
        else:
            self.sift_down(index)

    def heapify(self, arr):
        self.heap = arr[:]
        for i in range(len(arr)//2-1,-1,-1):
            self.sift_down(i)

    def heap_sort(self,arr):
        self.heapify(arr)
        sorted_arr = []
        size = self.get_size()
        while not self.is_empty():
            sorted_arr.append(self.extract_max())  # Extract max to sort
            size -= 1
        return sorted_arr[::-1]