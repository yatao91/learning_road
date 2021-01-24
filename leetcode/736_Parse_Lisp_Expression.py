# -*- coding: utf-8 -*-


def implicit_scope(func):
    def wrapper(*args):
        args[0].scope.append({})
        ans = func(*args)
        args[0].scope.pop()
        return ans
    return wrapper


class Solution(object):
    def __init__(self):
        self.scope = [{}]

    @implicit_scope
    def evaluate(self, expression):
        if not expression.startswith('('):
            if expression[0].isdigit() or expression[0] == '-':
                return int(expression)
            for local in reversed(self.scope):
                if expression in local:
                    return local[expression]

        tokens = list(self.parse(expression[5 + (expression[1] == 'm'): -1]))
        if expression.startswith('(add'):
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expression.startswith('(mult'):
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:
            for j in range(1, len(tokens), 2):
                self.scope[-1][tokens[j-1]] = self.evaluate(tokens[j])
            return self.evaluate(tokens[-1])

    def parse(self, expression):
        bal = 0
        buf = []
        for token in expression.split():
            bal += token.count('(') - token.count(')')
            buf.append(token)
            if bal == 0:
                yield " ".join(buf)
                buf = []
        if buf:
            yield " ".join(buf)


if __name__ == '__main__':
    expression = "(add 1 2)"
    print(Solution().evaluate(expression))
