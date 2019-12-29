# python3
import random


class HashNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class Hastable:
    def __init__(self):
        self.m = 10000000
        self.p = 10000019
        self.a = random.randint(0, self.p - 1)
        self.b = random.randint(1, self.p - 1)
        self.items = [None] * self.m

    def add(self, key, value):
        index = self.h(key)
        while self.items[index] != None:
            # update
            if self.items[index].key == key:
                self.items[index].value = value
                return
            index = self.__get_next_index(index)
        self.items[index] = HashNode(key, value)

    def get(self, key):
        index = self.h(key)
        while self.items[index] != None:
            if self.items[index].key == key:
                return self.items[index].value
            index = self.__get_next_index(index)
        return None

    def delete(self, key):
        index = self.h(key)
        while self.items[index] != None:
            if self.items[index].key == key:
                self.items[index] = None
            else:
                index = self.__get_next_index(index)

    def __get_next_index(self, index):
        index += 1
        if index == len(self.items):
            index = 0
        return index

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
