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

        temp = self.head
        while temp.next is not None:
            last = temp
            temp = temp.next
            temp.prev = last

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
        pass

    def popleft(self):
        pass

    def popright(self):
        pass

    def pushright(self, value):
        pass


if __name__ == "__main__":
    array = list(range(5))
    dll = DoublyLinkedList(array)
    print(dll)
