'''
Sorts an array in n steps, where n = size (number
of digits) of largest number in array. (If largest
number is 3,452, number of steps will be 4.)

First step uses counting sort to sort numbers in 
array by the values in their 'ones' positions. 

Second step uses counting sort to  sort numbers in 
array by the values of their 'tens' positions. 

...etc.








'''

from counting_sort import counting_sort

def radix_sort(arr):
    num_size = len(str(max(arr)))
    # print('num size: ', num_size)
    
    # for loop that applies counting sort to
    # each position in each number until you've
    # reached the max num_size

    for i in range(0, num_size): # tells number of loops we'll need
        # print('i in for loop: ', i)
        # isolate the 1's position, set as j
        j = '' # the position we want
        counting_sort(j)
        # indicate to move up to 10's posiiton?




if __name__=="__main__":
    array = [3, 17, 22, 144]

    radix_sort(array)