'''
iterates through array comparing current index(value)
to each subsequent index(value), searching for the
minimum value in the array. after a complete loop of
all unsorted items in the array, the current index is
swapped with the minimum index, such that smaller values
are sorted to the beginnin of the array.

steps:
1. set up loop to iterate over items in array
2. set current index as min index
3. compare all subsequent elements to current min index
4. if/when (/each time) a new min index is found, update
   `min_index` with that index
5. after a full loop through the array, swap the current
   index with the new min index
6. repeat until the full array is sorted.

requirements:
 - loop
 - var to store min index
 - mechanism to compare values
 - mechanism to swap current index/ min index
'''



def selection_sort(arr):












































def selection_sort(array, size):
    for i in range(0, size):
        min_index = i

        for j in range(i+1, size):
            if array[j] < array[min_index]:

                min_index = j

        (array[i], array[min_index]) = (array[min_index], array[i])

    return array


arr = [5,7,4,2,1,9]
size = len(arr)
print(f"input array: {arr}")

sorted_arr = selection_sort(arr, size)
print(f"sorted array: {sorted_arr}")



# # WHAT ABOUT ARRAY OF HIGH MED LOW
