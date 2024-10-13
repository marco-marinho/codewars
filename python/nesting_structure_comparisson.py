from collections.abc import Sequence


def is_scalar(x):
    return isinstance(x, str) or not isinstance(x, Sequence)


def same_structure_as(original, other):
    match original, other:
        case [[], []]:
            return True
        case [[*orig_elements], [*other_elements]]:
            if len(orig_elements) == len(other_elements):
                return all(
                    [
                        same_structure_as(x, y)
                        for x, y in zip(orig_elements, other_elements)
                    ]
                )
            return False
        case x, y:
            return is_scalar(x) and is_scalar(y)
        case _:
            return False
