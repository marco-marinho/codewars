def tree_by_levels(node):
    stack = [node] if node is not None else []
    output = []
    for curr in stack:
        output.append(curr.value)
        stack.extend(filter(lambda x: x is not None, [curr.left, curr.right]))
    return output
