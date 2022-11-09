
# # Procedural Programming

# x = 10
# y = 5

# result = x*y # 10 + 5 = 15

# result = result*2 # 15 * 2 = 30

# # print(result) # 30

# # OOP

# def add(a, b):
#     return a + b

# def mult_by_2(x):
#     return x*2

# result = add(x,y)

# result = mult_by_2(result)

# print(result)

class AMEmployee:

    _employer_name = "A.M. Money"

    def __init__(self, name):
        self.name = name

    def first_name(self):
        return self.name.split(' ')[0]

    @classmethod
    def employer_name(cls):
        return cls._employer_name

ellen = AMEmployee("Ellen Studer")

dan = AMEmployee("Dan Rogers")

print(ellen.name)

# print(ellen.first_name()) # Ellen (unique to each instance)
# print(ellen.employer_name()) # A.M. Money (unique to each class)

# print(dan.first_name()) # Dan (unique to each instance)
# print(dan.employer_name()) # A.M. Money (unique to each class)


