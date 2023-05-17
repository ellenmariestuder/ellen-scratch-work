'''
compare each number to the number left of it;
if it is smaller, swap it and put it ahead of that number.
(for the current index, keep swapping it until the number
 left of it is not greater.)

 1. establish loop to iterate through array (can start with i = 1)
 2. compare i to i-1;
    2.a if i-1 < i, pass
    2.b if i-1 > i, move to new loop
        2.b.1 if i-1 > i, swap i and i-1
        2.b.2 set index i as index j

last step is important: since i and j are _indexes_, once you swap
the values, index i is now pointing to its new value (previously the
value for j), rather than the index you want to keep comparing. in
order to continue tracking the number you started with,  you have to
update the index you're pointing to accordingly as you make swaps

'''

# input_array = [3,1,6,7,9,2,11]
input_array = [12, 7, 5, 3, 2]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            for j in reversed(range(0, i)):
                if arr[i] < arr[j]:
                    (arr[i], arr[j]) = (arr[j], arr[i])
                    i = j
    return arr

if __name__ == "__main__":
    print(input_array)
    sorted_array = insertion_sort(input_array)
    print(sorted_array)
