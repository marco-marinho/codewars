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
        print("rato")
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
    output = [0] * len(arr)
    root = None
    for idx, val in enumerate(arr[::-1]):
        print(val)
        output[idx], root = insert(root, val)
    return output[::-1]

print(smaller([408, -316, -165, -128, 44, -146, -208, -387, 474, 347, -294, 307, -492, -114, 81, 444, 321, -438, -181, -279, -398, 334, 444, 249, 21, -174, -61, -324, 461, 25, -152, 230, 297, 30, 67, 161, 255, 193, -68, 479, -257, -492, 145, 246, 219, -198, -412, 159, 453, 452, 241, -261, 367, -362, -408, -241, -175, 340, -251, 193, -338, -153, 389, -321, 62, 120, 65, -24, 46, 190, -309, -352, -141, 305, 195, -391, 115, 363, -363, -200, 261, -196, -311, 360, -325, -336, -86, -143, 177, 160, 409, -460, 395, 118, -313, -96, -319, 92, -318, 409, -303, 147, 145, 100, 197, 209, -85, 316, -438, 402, -309, 257, -234, -98, -55, 110, 500, 325, -262, -491, 310, 429, 129, 77, -38, 167, 409, -192, -70, 118, -294, 377, -381, 199, 8, -393, 92, -342, -479, -450, -360, -419, 137, -271, -216, -56, -117, 175, 90, 68, 253, -270, -381, -288, -77, -232, 198, 249, -238, -87, -431, 433, -129, -158, -47, 450, -241, 468, 88, 204, 279, 260, 448, 232, -363, 76, -189, -387, -258, -190, -156, 392, 434, -269, -379, -417, -5, 475, -30, 202, -494, -347, 67, 12, 211, -167, 492, 17, 47, 132, -90, 118, -321, -178, -355, -304, 463, 138, -262, -456, 375, 145, 102, 192, 118, -381, -270, 256, 252, 151, -233, 117, 496, 43, -227, 445, -121, -442, -49, -479, -70, 104, 308, -428, 58, 392, 291, 72, -297, -93, 217, -211, 149, 16, 36, 178, -395, -80, 18, 124, 85, -11, 207, -266, 81, 218, 64, 350, -489, -216, -452, -164, 109, -97, 54, -323, -32, -37, -11, -353, -220, 85, 142, -497, 71, 432, -102, -199, -35, -98, 346, -374, 168, -454, -159, 402, 473, -309, 370, -323, 481, 357, 396, -363, -5, -419, 11, -424, 75, -404, 49, -108, -258, 370, -455, 162, 455, 217, 433, -215, 44, 136, 457, -226, 357, -291, 435, 169, 103, -120, 74, -346, -493, 256, 152, 320, -204, -226, -33, 157, 284, -216, 168, 98, -434, -491, -35, -379, 453, -282, -99, 79, -42, -337, 204, -358, 185, -157, 18, 220, 439, -371, 153, -288, 46, -356, -126, 388, 445, -190, -322, 177, -372, 264, 327, -184, -362, -73, 270, -197, -401, 221, -445, 56, -203, 333, 382, 437, -89, 402, -321, -363, -318, -1, -298, 287, 484, 199, 194, -223, -387, 10, -114, -120, 131, -399, 390, -398, 323, -238, 149, 80, -222, 24, 228, 369, -398, 462, 104, -355, 320, -30, -33, 303, -361, -136, -175, 62, -101, -124, 481, 369, -112, 182, -472, 334, 268, 171, 471, 348, 215, 58, -297, -487, 43, -271, 24, -417, -57, 291, 453, 106, -25, -447, -42, 57, 485, 75, -217, -204, -225, 332, -230, -67, -242, -37]
))