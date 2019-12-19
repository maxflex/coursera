# python3

import sys
import threading


class Node:
    def __init__(self):
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def height(self) -> int:
        return self.__height(self.root)

    def __height(self, node) -> int:
        if node == None:
            return 0

        max_height = 0
        for child in node.children:
            height = self.__height(child)
            if height > max_height:
                max_height = height

        return 1 + max_height

    def __str__(self):
        print("======= TREE =======")
        self.__print(self.root)
        return ''

    def __print(self, node, level=0):
        if node == None:
            return

        print(id(node), "\tLevel: {}".format(level))
        self.__print(node.left, level + 1)
        self.__print(node.right, level + 1)


def main():
    n = int(input())
    parent_indexes = list(map(int, input().split()))

    nodes = []
    for i in range(n):
        nodes.append(Node())

    for i in range(n):
        parent_index = parent_indexes[i]
        if parent_index == -1:
            tree = BinaryTree(nodes[i])
        else:
            nodes[parent_index].add_child(nodes[i])

    print(tree.height())
    # print(tree)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
