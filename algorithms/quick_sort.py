def quick_sort(arr, start, end):
    if start < end:
        partit = start
        pivot = arr[end]

        for i in range(start, end):
            if arr[i] < pivot:
                arr[partit], arr[i] = arr[i], arr[partit]
                partit += 1
        arr[partit], arr[end] = arr[end], arr[partit]

        quick_sort(arr, start, partit-1)
        quick_sort(arr, partit+1, end)

if __name__=="__main__":
    array = [4, 7, 9, 2, 3, 1, 6, 5]
    print("unsorted array: ", array)
    quick_sort(array, 0, len(array)-1)
    print("sorted array: ", array)

# SORTED ARRAY SHOULD BE: 1, 2, 3, 4, 5, 6, 7, 9
