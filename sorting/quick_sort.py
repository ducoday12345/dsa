class QuickSort:
    def __init__(self, arr: list):
        self.arr = arr
        
    def quick_sort(self,  low:int, high:int):
        if low<high:
            pi = self.partition(low,high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)
    
    def partition(self,low:list, high: list):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i],self.arr[j] = self.arr[j],self.arr[i]
        self.arr[i+1],self.arr[high] = self.arr[high],self.arr[i+1]
        return i+1
            

if __name__ == "__main__":
    arr = [2, 8, 5, 3, 9, 4, 1, 7]
    sorter = QuickSort(arr)
    
    sorter.quick_sort(0,len(arr)-1)
    print(f"Sorted array: {arr}")