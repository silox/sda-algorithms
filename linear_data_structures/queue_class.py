from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def first(self):
        pass

    def is_empty(self):
        pass


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(42)
    queue.enqueue(10)
    print(queue.first())
    print(queue.first(), queue.dequeue())
    print()

    for i in range(10):
        queue.enqueue(i)

    queue2 = Queue()
    print(queue.queue)
    while not queue.is_empty():
        queue2.enqueue(queue.dequeue())

    print(queue2.queue)
