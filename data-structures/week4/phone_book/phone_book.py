# python3
import random


class HashNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class Hastable:
    def __init__(self):
        self.m = 1000
        self.p = 10000019
        self.a = random.randint(0, self.p - 1)
        self.b = random.randint(1, self.p - 1)
        self.items = [HashNode()] * self.m

    def add(self, key, value):
        index = self.h(key)
        item = self.items[index]

        while True:
            if item.key == key:
                item.value = value
                return
            if item.next is None:
                item.next = HashNode(key, value)
                return
            item = item.next

    def get(self, key, delete=False):
        index = self.h(key)
        item = self.items[index]

        while item.key != key and item.next != None:
            if delete is True:
                prev = item
            item = item.next

        if item.key == key:
            if delete is True:
                prev.next = item.next
            else:
                return item.value

        return None

    def delete(self, key):
        self.get(key, True)

    def h(self, key):
        return (self.a * key + self.b) % self.p % self.m


def main():
    h = Hastable()
    n = int(input())
    for _ in range(n):
        line = input().split()
        command = line[0]
        key = int(line[1])
        if command == 'add':
            h.add(key, line[2])
        elif command == 'find':
            result = h.get(key)
            print('not found' if result is None else result)
        else:
            h.delete(key)

    # while True:
    #     [command, key] = input().split()
    #     key = int(key)
    #     if command == 'add':
    #         h.add(key, input())
    #     elif command == 'del':
    #         h.delete(key)
    #     else:
    #         print(h.get(key))


if __name__ == '__main__':
    main()
