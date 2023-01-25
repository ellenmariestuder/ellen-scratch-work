numbers = [1,3,4,5,5,6,7,7,6,8]

def multiply_x2(number):
    return number*2

# for number_index in range(0, len(numbers)):
#     numbers[number_index] = multiply_x2(numbers[number_index])

numbers = map(lambda x:x*2, numbers)
print(list(numbers))



# a = 5
# b = 7
# a == b

# print(a==b)