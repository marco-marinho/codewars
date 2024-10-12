class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 0
        self.dup = 1


def insert(root, value, count=0):
    if root is None:
        return count, Node(value)
    if root.value == value:
        root.dup += 1
        return count + root.count, root
    if root.value < value:
        count, root.right = insert(root.right, value, count + root.count + root.dup)
        return count, root
    else:
        root.count += 1
        count, root.left = insert(root.left, value, count)
        return count, root


def smaller(arr):
    output = [0] * len(arr)
    root = None
    for idx, val in enumerate(arr[::-1]):
        output[idx], root = insert(root, val)
    return output[::-1]
