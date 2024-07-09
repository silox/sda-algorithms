class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return f'Node({self.data}, {self.next})'


class DoublyLinkedList:
    def __init__(self, array=None):
        self.head = None
        self.tail = None
        self.count = 0
        if array is None:
            return

        self.head = self.tail = Node(array[-1])
        for value in array[-2::-1]:
            self.head = Node(value, self.head)
            self.head.next.prev = self.head

        self.count = len(array)

    def __str__(self):
        """
        Returns: String representation of linked list in format
        a1 -> a2 -> ... -> None
        """
        result_list = []
        temp = self.head
        while temp is not None:
            result_list.append(str(temp.data))
            temp = temp.next

        return ' <-> '.join([*result_list, str(None)])

    def __len__(self):
        return self.count

    def pushleft(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, self.head)
            self.head.next.prev = self.head

        self.count += 1

    def popleft(self):
        if self.head is None:
            raise IndexError('Linked list is empty')

        result = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.count -= 1
        return result

    def popright(self):
        if self.tail is None:
            raise IndexError('Linked list is empty')

        result = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.count -= 1
        return result

    def pushright(self, value):
        if self.tail is None:
            self.head = self.tail = Node(value)
        else:
            self.tail = Node(value, prev=self.tail)
            self.tail.prev.next = self.tail

        self.count += 1

    def sum(self):
        pass  # TODO

    def max(self):
        pass  # TODO

    def min(self):
        pass  # TODO


if __name__ == "__main__":
    array = list(range(5))
    dll = DoublyLinkedList(array)
    print(dll, len(dll))
    dll.pushright(10)
    print(dll, len(dll))
    print(dll.popleft())
    print(dll, len(dll))
    print(dll.popright())
    print(dll, len(dll))
    dll.pushleft(20)
    print(dll, len(dll))

    try:
        while True:
            print(dll.popright())
    except IndexError:
        print(dll, len(dll))

    dll.pushright(100)
    print(dll, len(dll))
    print(dll.popleft())
    print(dll, len(dll))
    dll.pushleft(200)
    print(dll, len(dll))

    dll2 = DoublyLinkedList()
    print(dll2, len(dll2))
    dll2.popright()
