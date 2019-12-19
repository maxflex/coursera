# python3


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Bracket:
    opening = '[({'
    closing = '])}'

    @staticmethod
    def is_same_type(opening_bracket, closing_bracket):
        return Bracket.opening.find(opening_bracket) == Bracket.closing.find(closing_bracket)


def solve(text: str):
    stack = Stack()
    for index, char in enumerate(text, 1):
        if char in Bracket.closing:
            if stack.is_empty() or not Bracket.is_same_type(stack.pop()['char'], char):
                return index

        if char in Bracket.opening:
            stack.push({
                'char': char,
                'index': index
            })

    return "Success" if stack.is_empty() else stack.peek()['index']


def main():
    print(solve(input()))


if __name__ == "__main__":
    main()
