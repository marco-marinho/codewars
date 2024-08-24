class Node:

    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None
        self.size = 1


def height(root):
    return 0 if root is None else root.height


def size(root):
    return 0 if root is None else root.size


def rotate_left(root):
    next_root = root.right
    if next_root is None:
        return root
    temp = next_root.left

    next_root.left = root
    root.right = temp

    root.height = 1 + max(height(root.left), height(root.right))
    next_root.height = 1 + max(height(next_root.left), height(next_root.right))

    root.size = 1 + size(root.left) + size(root.right)
    next_root.size = 1 + size(next_root.left) + size(next_root.right)
    return next_root


def rotate_right(root):
    next_root = root.left
    if next_root.right is None:
        return root
    temp = next_root.right

    next_root.right = root
    root.left = temp

    root.height = 1 + max(height(root.left), height(root.right))
    next_root.height = 1 + max(height(next_root.left), height(next_root.right))

    root.size = 1 + size(root.left) + size(root.right)
    next_root.size = 1 + size(next_root.left) + size(next_root.right)
    return next_root


def insert(root, value, count=0):
    if root is None:
        return 0, Node(value)
    elif value <= root.value:
        count, root.left = insert(root.left, value, count)
    else:
        count, root.right = insert(root.right, value, count)
        count += size(root.left) + 1

    lheight = height(root.left)
    rheight = height(root.right)

    root.height = max(lheight, rheight) + 1
    root.size = 1 + size(root.left) + size(root.right)
    balance = lheight - rheight

    # Left rotation
    if balance > 1 and value < root.left.value:
        return count, rotate_right(root)

    # Right rotation
    if balance < -1 and value > root.right.value:
        return count, rotate_left(root)

    # Left-Right rotation
    if balance > 1 and value > root.left.value:
        root.left = rotate_left(root.left)
        return count, rotate_right(root)

    # Right-Left rotation
    if balance < -1 and value < root.right.value:
        root.right = rotate_right(root.right)
        return count, rotate_left(root)

    return count, root


def smaller(arr):
    arr = arr * 10
    output = [0] * len(arr)
    root = None
    for idx, val in enumerate(arr[::-1]):
        output[idx], root = insert(root, val)
    return output[::-1]
