# python3


class HashNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class Hastable:
    def __init__(self, m):
        self.m = int(m)
        self.p = 1000000007
        self.x = 263
        self.items = [HashNode() for _ in range(m)]

    def add(self, key, value):
        index = self.h(key)
        # print("Inserting {} at index {}".format(value, index))
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

    def check(self, index):
        output = []
        item = self.items[int(index)]
        while item.next != None:
            item = item.next
            output.append(item.value)
        output.reverse()
        print(" ".join(output))

    def delete(self, key):
        self.get(key, True)

    def h(self, key):
        s = sum([ord(key[i]) * (self.x ** i) for i in range(len(key))])
        return s % self.p % self.m


def main():
    h = Hastable(int(input()))
    n = int(input())
    for _ in range(n):
        command, param = input().split()
        if command == 'add':
            h.add(param, param)
        elif command == 'find':
            result = h.get(param)
            print('no' if result is None else 'yes')
        elif command == 'check':
            h.check(param)
        else:
            h.delete(param)

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
