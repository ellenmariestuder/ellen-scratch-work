arr = [5,7,4,2,1,9]

size = len(arr)

def selection_sort(array, size):
    for i in range(0, size):
        min_index = i

        for j in range(i+1, size):
            if array[j] < array[min_index]:

                min_index = j

        (array[i], array[min_index]) = (array[min_index], array[i])

    return array





print(f"input array: {arr}")

sorted_arr = selection_sort(arr, size)

print(f"sorted array: {sorted_arr}")











































# print(f"input array: {arr}")

# def selection_sort(array):
#     for i in range(len(array)):
#         min_index = i

#         for j in range(i+1, len(array)):
#             if array[j] < array[min_index]:
#                 min_index = j

#         (array[i], array[min_index]) = (array[min_index], array[i])
#     return array

# arr2 = selection_sort(arr)

# print(f"sorted array: {arr2}")


# # WHAT ABOUT ARRAY OF HIGH MED LOW
