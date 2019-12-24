# python3
import math


class Thread:
    def __init__(self, index, free_at):
        self.index = index
        self.free_at = free_at


class MinHeap:
    def __init__(self, n):
        self.threads = [Thread(i, 0) for i in range(n)]

    def process(self, time):
        print("{} {}".format(self.threads[0].index, self.threads[0].free_at))
        self.threads[0].free_at += time
        self.sift_down(0)

    def sift_down(self, index):
        min_index = index

        left_index = 2 * index + 1
        right_index = left_index + 1

        if self.node_exists(left_index):
            if self.needs_swap(min_index, left_index):
                min_index = left_index
            if self.node_exists(right_index) and self.needs_swap(min_index, right_index):
                min_index = right_index

        if min_index != index:
            self.threads[index], self.threads[min_index] = self.threads[min_index], self.threads[index]
            self.sift_down(min_index)

    def needs_swap(self, index, swap_index):
        node = self.threads[index]
        swap = self.threads[swap_index]

        if swap.free_at < node.free_at:
            return True
        if swap.free_at == node.free_at and swap.index < node.index:
            return True
        return False

    def node_exists(self, index) -> bool:
        return index < len(self.threads)

    def is_leaf_node(self, index) -> bool:
        return index >= math.floor(len(self.threads) / 2)


def main():
    [n, m] = list(map(int, input().split()))
    times = list(map(int, input().split()))
    heap = MinHeap(n)
    for time in times:
        heap.process(time)


if __name__ == '__main__':
    main()
