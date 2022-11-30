def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


a = [85, 42, 99, 15]
print('unsorted array: ', a)

bubble_sort(a)
print('sorted array: ', a)
