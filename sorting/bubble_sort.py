def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for i in range(0, n-i-1):
            if  arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
        if flag == False: break

if __name__ == "__main__":
    arr = [2, 8, 5, 3, 9, 4, 1, 7]
    bubble_sort(arr)
    print(f"Sorted array: {arr}")