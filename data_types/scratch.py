# stacks and queues are also lists in python

# queue
# (think of a line at a movie theater)
# - ordered
# - FIFO
# - takes different data types (heterogeneous)
my_queue = list()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

print('queue: ', my_queue)
my_queue.pop(0)
print('queue (popped): ', my_queue)
my_queue.pop(0)
print('queue (popped x2): ', my_queue)

# stack
# (think a stack of books)
# - ordered
# - FILO
# - takes different data types
my_stack = list()
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
# print('stack: ', my_stack)
my_stack.pop()
# print('stack (popped): ', my_stack)
my_stack.pop()
# print('stack (popped x2): ', my_stack)

# list
# - ordered
# - takes different data types
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
# print('list: ', my_list)


# like lists, you can access any item in a stack or que 
# by referencing the index