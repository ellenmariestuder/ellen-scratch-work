
def selection_sort(array, size):
    for i in range(size):
        min_index = i    # space = constant
        x = i*2          # space = c (so now 2c)
        new_arr = array  # space = n (n refers to size of input array) 
                         # new total space = n+c
        # print(f'starting index: ', min_index)
        # print(f'starting index value: ', array[i])

        for j in range(i+1, size):
            # print(f'comparing index value: ', array[j])
            if array[j] < array[min_index]:
                min_index = j
                # print(f'new min index: ', min_index)
            
        (array[i], array[min_index]) = (array[min_index], array[i])

# WHAT ABOUT ARRAY OF HIGH MED LOW



a = [1,5,4,2,7]
s = len(a)
print(f'original array: ', a)

selection_sort(a, s)
print(f'sorted array: ', a)

# space = 1c (1 x constant)
# convention is to negate the constant (the 1).
# so space = c

# asymptotic space complexity
# (asymptotic just means not discrete)
# big O = O(1)

# if it's just constants then it will be O(1)
# doesn't matter how many constants-- will always be 1

# (n[n+1])/2  <- arithmatic sequence proof