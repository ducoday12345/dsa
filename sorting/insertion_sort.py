def insertion_sort(arr:list):
    for i in range(1, len(arr)-1):
        j = i
        while j > 0 and arr[j-1]> arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

if __name__ == "__main__":
    arr = [2, 8, 5, 3, 9, 4, 1, 7]
    insertion_sort(arr)
    print(f"Sorted array: {arr}")