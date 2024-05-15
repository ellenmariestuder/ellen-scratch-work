numbers = [13, 456, 24, 47, 13, 84, 456]

# filter list to only include odd numbers
# odd_numbers = list(filter(lambda d: d%2 != 0, numbers))
odd_numbers = filter(lambda d: d%2 != 0, numbers)
# print(odd_numbers)

# print(next(odd_numbers))
# print(next(odd_numbers))

x = range(0, 10)
print(type(x))

# generators lazily evaluate elements of a sequence 
# ^^ aka iterator
# ^^ generator is a type, like scalar and compound
# ^^ examples are: filter, map, reduce, etc
# ^^ 
# ^^ type is a million things. it's an instance of a class, an object, etc.

def is_cool():
    return False

def is_funny():
    return False

if is_cool() and is_funny():
    print("Gets invited to party!")

# ^ Strict evaluation (default for python): only evaluates as far as it needs to;
#   (i.e if first condition returns false then no need to proceed to subseequent 
#    conditions)

# ---------------------------------------------------------------------------------

nums = [3,45,2,67,73]

# def is_even(num):
#     return (num % 2)==0 

# filter(is_even, nums)
# filter(lambda num: (num % 2)==0, nums)


# def multiply_by_2(num):
#     return num*2

# map(multiply_by_2, nums)


bigger_nums = map(lambda num: num*2, nums)

print(next(bigger_nums))