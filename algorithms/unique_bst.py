def num_trees(n):
    num_tree = [1] * (n + 1)

    for nodes in range (2, n + 1):
        total  = 0
        for root in range(1, nodes + 1):
            left  = root - 1
            right = nodes - root
            total += num_tree[left] * num_tree[right]
        num_tree[nodes] = total

    return num_tree[n]

# def num_trees(n):
#     num_tree = [1] * (n + 1)
#     print(num_tree)

#     for nodes in range (2, n + 1):
#         print('nodes' , nodes, ' -------------------------- ')
#         print('  num_tree (start)...', num_tree)
#         total  = 0
#         for root in range(1, nodes + 1):
#             print('     roots', root)
#             left  = root - 1
#             print('         left: ', left)
#             right = nodes - root
#             print('         right:', right)
#             total += num_tree[left] * num_tree[right]
#             print('     TOTAL: ', total)
#         num_tree[nodes] = total
#         print('  num_tree (end)...', num_tree)
#         print('\n')

#     return num_tree[n]

# print(num_trees(4))
