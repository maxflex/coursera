# python3
import math


class MinHeap:
    def __init__(self, items):
        self.items = items
        self.swaps = []
        self.__min_heapify()

    def __min_heapify(self, index=0):
        if self.is_leaf_node(index):
            return

        left_index = 2 * index + 1
        right_index = left_index + 1

        for i in [left_index, right_index]:
            if self.node_exists(i):
                self.__min_heapify(i)

        swap_index = right_index if self.node_exists(
            right_index) and self.items[right_index] < self.items[left_index] else left_index

        # swap only if heap condition not satisfied
        if self.items[swap_index] < self.items[index]:
            self.items[index], self.items[swap_index] = self.items[swap_index], self.items[index]
            self.swaps.append([index, swap_index])
            self.__min_heapify(swap_index)

    def print_swaps(self):
        print(len(self.swaps))
        for swap in self.swaps:
            print(" ".join(map(str, swap)))

    def node_exists(self, index) -> bool:
        return index < len(self.items)

    def is_leaf_node(self, index) -> bool:
        return index >= math.floor(len(self.items) / 2)


def main():
    input()
    items = list(map(int, input().split()))
    heap = MinHeap(items)
    heap.print_swaps()


if __name__ == '__main__':
    main()
