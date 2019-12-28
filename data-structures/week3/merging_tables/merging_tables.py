# python3


class DisjointSet:
    def __init__(self, values):
        self.max = -1
        self.parents = []
        self.values = values

        for index, value in enumerate(values):
            self.parents.append(index)
            if value > self.max:
                self.max = value

    def union(self, index_to, index_source):
        indexes_in_the_way = []
        while self.parents[index_to] != index_to:
            indexes_in_the_way.append(index_to)
            index_to = self.parents[index_to]

        # cache path
        for index in indexes_in_the_way:
            self.parents[index] = index_to

        indexes_in_the_way = []
        while self.parents[index_source] != index_source:
            indexes_in_the_way.append(index_source)
            index_source = self.parents[index_source]

        # cache path
        for index in indexes_in_the_way:
            self.parents[index] = index_source

        if index_to != index_source:
            self.parents[index_source] = index_to
            self.values[index_to] += self.values[index_source]
            if self.values[index_to] > self.max:
                self.max = self.values[index_to]

        print(self.max)


class Query:
    def __init__(self, to, source):
        self.to = to - 1
        self.source = source - 1


def main():
    [_, n] = list(map(int, input().split()))
    sizes = list(map(int, input().split()))

    disjoint_set = DisjointSet(sizes)

    queries = []
    for _ in range(n):
        [to, source] = list(map(int, input().split()))
        queries.append(Query(to, source))

    for query in queries:
        disjoint_set.union(query.to, query.source)


if __name__ == '__main__':
    main()
