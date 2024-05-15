class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


root = Node(5)
new_left = Node(3)
new_right = Node(8)
root.left  = new_left
root.right = new_right


def levelordertraversal(root):
    if not root:
        return []
    
    queue = []
    queue.append(root)

    while queue:
        print(queue[0].value)
        node = queue.pop(0)
        # print(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print(levelordertraversal(root))