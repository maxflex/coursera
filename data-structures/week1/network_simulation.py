# python3


class Queue:
    def __init__(self, size):
        self.items = [None] * size
        self.size = size
        self.current = 0
        self.next = 0

    def enqueue(self, item):
        assert not self.is_full()
        self.items[self.next] = item
        self.next = self.__next_index(self.next)

    def dequeue(self):
        assert not self.is_empty()
        item = self.items[self.current]
        self.items[self.current] = None
        self.current = self.__next_index(self.current)
        return item

    def peek(self):
        return self.items[self.current]

    def is_empty(self) -> bool:
        return self.items[self.current] is None

    def is_full(self) -> bool:
        return not self.is_empty() and not self.items[self.next] is None

    def __next_index(self, index):
        next_index = index + 1
        return next_index if next_index < self.size else 0


class Packet:
    def __init__(self, arrived_at, duration):
        self.arrived_at = arrived_at
        self.duration = duration


def main():
    buffer_size, n = list(map(int, input().split()))
    queue = Queue(buffer_size)

    packets = []
    for _ in range(n):
        arrived_at, duration = list(map(int, input().split()))
        packets.append(Packet(arrived_at, duration))

    # when the cpu gets free
    cpu_free_at = 0

    for packet in packets:
        while not queue.is_empty() and queue.peek()['finish_at'] <= packet.arrived_at:
            queue.dequeue()

        if queue.is_full():
            print('-1')
        else:
            start_at = max(cpu_free_at, packet.arrived_at)
            finish_at = start_at + packet.duration
            queue.enqueue({
                'start_at': start_at,
                'finish_at': finish_at,
            })
            cpu_free_at = finish_at
            print(start_at)


if __name__ == '__main__':
    main()
