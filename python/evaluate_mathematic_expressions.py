import re

token_re = re.compile(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])")


class Binary:
    def __init__(self, left, op, right) -> None:
        self.left = left
        self.op = op
        self.right = right

    def solve(self):
        if self.op == "+":
            return self.left.solve() + self.right.solve()
        if self.op == "-":
            return self.left.solve() - self.right.solve()
        if self.op == "*":
            return self.left.solve() * self.right.solve()
        if self.op == "/":
            return self.left.solve() / self.right.solve()


class Unary:
    def __init__(self, op, right) -> None:
        self.op = op
        self.right = right

    def solve(self):
        return -self.right.solve()


class Group:
    def __init__(self, right) -> None:
        self.right = right

    def solve(self):
        return self.right.solve()


class Number:
    def __init__(self, value) -> None:
        self.value = value

    def solve(self):
        return self.value


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.pos = 0

    def term(self):
        expr = self.factor()

        while self.match("+", "-"):
            op = self.previous()
            right = self.factor()
            expr = Binary(expr, op, right)

        return expr

    def factor(self):
        expr = self.unary()

        while self.match("*", "/"):
            op = self.previous()
            right = self.unary()
            expr = Binary(expr, op, right)

        return expr

    def unary(self):
        if self.match("-"):
            op = self.previous()
            right = self.unary()
            return Unary(op, right)

        return self.primary()

    def primary(self):
        if self.match("("):
            expr = self.term()
            self.advance()
            return Group(expr)
        return Number(int(self.advance()))

    def match(self, *args):
        if self.pos >= len(self.tokens):
            return False
        for arg in args:
            if self.tokens[self.pos] == arg:
                self.advance()
                return True
        return False

    def advance(self):
        if self.pos < len(self.tokens):
            self.pos += 1
        return self.previous()

    def previous(self):
        return self.tokens[self.pos - 1]


def calc(expression):
    tokens = token_re.findall(expression)
    parser = Parser(tokens)
    return parser.term().solve()
