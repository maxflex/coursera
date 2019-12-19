# python3

import math


class Stack:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        self.max.append(item if self.is_empty() or item >
                        self.max[-1] else self.max[-1])
        self.items.append(item)

    def pop(self):
        assert not self.is_empty()
        self.max.pop()
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def get_max(self):
        assert not self.is_empty()
        return self.max[-1]

    def is_empty(self):
        return len(self.items) == 0


def main():
    n = int(input())

    stack = Stack()

    for _ in range(n):
        command = input()
        if command == 'pop':
            stack.pop()
        elif command == 'max':
            print(stack.get_max())
        else:
            stack.push(int(command.split()[1]))


if __name__ == '__main__':
    main()
