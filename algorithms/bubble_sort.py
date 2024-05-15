'''
iterates through array
compares two side-by-side numbers at a time
does 1-1 swap if a greater value precedes a lesser value

steps:
1. compare current value to value behind it
2. if value behind it is less than current value, swap indices
3. continue this compare/swap until the end of the array
4. start over at beginning of array; repeat steps 1-3

requirements:
1. loop that iterates through array (always starts with arr[0])
2. mechanism to compare current value to value behind it
3. mechanism to swap values if appropriate
4. mechanism to move forward/ start over as appropriate


INSIGHTS:
Initially I just had the inner loop. It successfully iterated
through the array once and performed the correct swaps as expected.
I was a little stumped as to how to get it to start over and keep
running that loop until the array was sorted though.

I tried adding an outer loop knowing that some other mechanism had to
tell this loop to run again until the end of the array was reached.
I was confused about how I would tell this outer array to initiate the
loop from index 0 each time though.

I ended up just implementing the outer loop the same way i did the
inner loop-- setting it to iterate over the length of the array (-1).
I didn't think this would work because I though that by setting it up
this way, at each iteration it would start at the present index rather
than starting over from index 0 like I wanted.

Surprisingly, It did what I wanted though! So I implemented all the
comments below to examine what was happening at each iteration and loop
through the array. What it reveals is this: Because the _inner_ loop
specifies range(0 - size), it starts at the 0th index each time it is
called. If it were to specify range(i - size) or range(z - size), _then_
it would be starting at the current incrementation each time. But that's
not how the code is set up.

'''




# def bubble_sort(arr):
#     # outer for-loop: for each index in 0 - (length of array -1):
#     for z in range(0, len(arr)-1):
#         print(f"\nstarting loop; z = {arr[z]} (index = {z})------------------------")
#         # inner for-loop: for each index in 0 - (length of array -1 -z)
#         # (-z because we don't have to sort through already-sorted items)
#         for i in range(0, (len(arr)-1-z)):
#             # set subsequent index as j
#             j = i+1
#             print(f"\nlooping; i = {arr[i]} (index {i}); j = {arr[j]} (index {j})")
#             print(f"current arr: {arr}")
#             # compare current index and subsequent index
#             # if current index value is greater than subsequent index value
#             if arr[i] > arr[j]:
#                 # swap the two values in the array
#                 (arr[i], arr[j]) = (arr[j], arr[i])
#                 print(f"swapped arr: {arr}")
#             else: print(f"nothing to swap")

#     return arr


# array = [5,7,4,2,1,9]
# print(f"input array: {array}")

# sorted_array = bubble_sort(array)
# print(f"sorted array: {sorted_array}")










array = [5,7,4,2,1,9]

for i in range(0, len(array)):
    print('this is i---------- ')
    print(array[i])
    j = i-1
    for j in range(i, 0):
        print('    this is j---------- ')
        print('    ', array[j])
        j =- 1

