class Nonsense(int):
    def __call__(self, other):
        return Nonsense(self + other)


def add(n):
    return Nonsense(n)
