def selection_sort(arr: list):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
if __name__ == "__main__":
    arr = [2,8,5,3,9,4,1]
    print(selection_sort(arr))