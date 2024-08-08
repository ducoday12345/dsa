class BinarySearch:
    def __init__(self, arr: list):
        self.arr= arr

    #iterative binary search implementation
    def BinarySearch(self, target: int):
        left = 0
        right = len(self.arr) - 1
        while left <= right:
            mid = (left+right)//2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                right = mid
            elif self.arr[mid] < target:
                left = mid
        return -1
    
    #recursive binary search implementation
    def BinarySearchRecursive(self, target: int):
        
        return self._recursive_search_helper( target, 0, len(self.arr)-1)
    
    #private (helper) class for BinarySearchRecursive
    def _recursive_search_helper(self, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if self.arr[mid] == target:
            return mid
        elif self.arr[mid] < target:
            return self._recursive_search_helper(target, mid, right)
        elif self.arr[mid] > target:
            return self._recursive_search_helper(target, left, mid)