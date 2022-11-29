
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # print('array: ', array)       # THESE DON'T GET PRINTED
        # print(f'array[i]: ', array[i])
        for j in (0, n-i-1):
            print('array: ', array)
            print(f'array[i]: ', array[i])
            print(f'array[j]: ', array[j])
            if array[j] > array[j+1]:
                print(f'array[j+1]: ', array[j+1])
                array[j], array[j+1] = array[j+1], array[j]
                print(f'new array[j]: ', array[j])
                print(f'new array[j+1]: ', array[j+1])
                print('start over')


a = [85, 42, 99, 15]

# print(f'unsorted array: ', a)

bubble_sort(a)
# print(f'sorted array: ', a)


# why is it jumping to the last array item (15/ 3) upon
# the next iteration?