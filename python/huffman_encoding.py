import heapq
from collections import Counter


class LeafNode:


    __match_args__ = ("weight", "value")

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.weight < other.weight


class InternalNode:
    __match_args__ = ("weight", "left", "right")

    def __init__(self, weight, left, right):
        self.weight = weight
        self.left = left
        self.right = right
        self.parent = None

    def __lt__(self, other):
        return self.weight < other.weight


def gen_tree(freqs):
    h = []
    for entry in freqs:
        heapq.heappush(h, LeafNode(entry[1], entry[0]))

    while len(h) > 1:
        right = heapq.heappop(h)
        left = heapq.heappop(h)
        new_node = InternalNode(right.weight + left.weight, left, right)
        right.parent = new_node
        left.parent = new_node
        heapq.heappush(h, new_node)

    return h[0]


def frequencies(s):
    return Counter(s).items()


def encode(freqs, s):
    if len(freqs) < 2:
        return None
    tree = gen_tree(freqs)
    queue = [(tree, "")]
    encode_table = {}
    while queue:
        node, code = queue.pop()
        match node:
            case LeafNode(_, value):
                encode_table[value] = code
            case InternalNode(_, left, right):
                queue.append((left, code + "0"))
                queue.append((right, code + "1"))
    return "".join(encode_table[entry] for entry in s)


def decode(freqs, bits):
    if len(freqs) < 2:
        return None
    output = ""
    tree = gen_tree(freqs)
    curr = tree
    for entry in bits:
        if entry == "0":
            node = curr.left
        else:
            node = curr.right
        match node:
            case LeafNode(_, value):
                output += value
                curr = tree
            case InternalNode(_, _, _):
                curr = node
    return output
