# python3


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
        return -1 if self.is_empty() else self.max[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        self.s1.push(value)

    def print_max(self):
        print(max(self.s1.get_max(), self.s2.get_max()), end=' ')

    def dequeue(self):
        assert not (self.s1.is_empty() and self.s2.is_empty())

        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

        return self.s2.pop()


def main():
    n = int(input())
    values = list(map(int, input().split()))
    m = int(input())
    q = Queue()

    for i in range(m):
        q.enqueue(values[i])
    q.print_max()

    for i in range(n - m):
        q.enqueue(values[i + m])
        q.dequeue()
        q.print_max()


if __name__ == '__main__':
    main()
