from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

    def next(self):
        return self.queue[0]

    def is_empty(self):
        return not self.queue


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(42)
    queue.enqueue(10)
    print(queue.next())
    print(queue.dequeue(), queue.dequeue())
    print()

    for i in range(10):
        queue.enqueue(i)

    queue2 = Queue()
    print(queue.queue)
    while not queue.is_empty():
        queue2.enqueue(queue.dequeue())

    print(queue2.queue)
