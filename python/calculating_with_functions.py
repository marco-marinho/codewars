import operator


def num_template(value):
    def inner(args=None):
        if args is None:
            return value
        operator, other = args
        return operator(value, other)

    return inner


def operation_template(operation):
    def inner(left):
        return operation, left

    return inner


zero = num_template(0)
one = num_template(1)
two = num_template(2)
three = num_template(3)
four = num_template(4)
five = num_template(5)
six = num_template(6)
seven = num_template(7)
eight = num_template(8)
nine = num_template(9)

plus = operation_template(operator.add)
minus = operation_template(operator.sub)
times = operation_template(operator.mul)
divided_by = operation_template(operator.ifloordiv)
