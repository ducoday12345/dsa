class Merge_sort:
    def __init__(self, arr: list):
        self.arr = arr
        
    def merge_sort(self, arr = None):
        if arr is None:
            arr = self.arr

        if len(arr) <= 1:
            return arr
    
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        left_part = self.merge_sort(left)
        right_part = self.merge_sort(right)

        return self.merge(left_part, right_part)
    
    def merge(self, l:list, r : list):
        i = 0
        j = 0
        res = []
        while i< len(l) and j < len(r):
            if l[i] <=  r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        if i < len(l) :
            res.extend(l[i:])
        if j < len(r) :
            res.extend(r[j:])
        return res

if __name__ == "__main__":
    arr = [2, 8, 5, 3, 9, 4, 1, 7]
    sorter = Merge_sort(arr)
    
    sorted_array = sorter.merge_sort()
    print(f"Sorted array: {sorted_array}")