'''
Counting Sort

Takes array of (small) numbers, counts number of times
each value appears in the array, and then populates sorted
new array based on indexes and value counts.

Steps:
1. create empty index of 0-9
2. create empty output array
2. loop through input array, increment count in the
   index array for the respective value each time it
   appears in the array
3. loop through index array, add value of i to i+1
4.
    a. loop through input again. for each value, look at
       the corresponding INDEX in the index array. for the
       VALUE associated with that INDEX, place the current
       i value in the PLACE (in your sorted output array)
       that matches the VALUE in the index array (-1) (< to
       account for the 0 place). then decrement the value 
       in the index array by one.

'''

array = [3, 3, 1, 7, 2, 8, 7]

def counting_sort(arr):
    max_num = max(arr)

    index_arr = [0] * (max_num+1)
    # ^ index array = max_num+1 because we only need as many spaces as there
    #   are *unique* values (the +1 is to account for the '0' position)
    output_arr = [0] * len(arr)

    # for each value in the input array, increment the corresponding index 
    # in the index array by 1
    for number in arr:
        index_arr[number] += 1
    print('input array:    ', arr)
    print('expected output: [1, 2, 3, 3, 7, 7, 8]')
    print('index array:                ', index_arr)

    # create running sum in index_arr
    for i in range(1, len(index_arr)):
        index_arr[i] += index_arr[i-1]
    print('index array (running sum): ', index_arr)

    # place values from input array in appropriate indexes in output array by
    # placing the number at the output array index equal to input_array[number]-1. 
    # meaning, where the index array index matches the current number of the 
    # input array, the corresopnding index array *value* -1 will be the index of
    # the number in the output array. (the -1 is to account for the 0 place).
    # at the end of each loop, decrement the value for this number in the index
    # array so that subsequent loops over the same number (for those that appear
    # more than once) will be appropriately placed at the correct index
    for number in arr:
        print('-------starting loop-------')
        print('number: ', number)
        print('index_arr[number]: ', index_arr[number])
        print('index array: ', index_arr)
        output_arr[(index_arr[number]-1)] = number
        index_arr[number] -= 1
        print('output_arr', output_arr)
        print('\n')
    
    return output_arr

if __name__ == "__main__":
    counting_sort(array)

