class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'Node({self.data}, {self.next})'


class LinkedList:
    def __init__(self, array):
        self.head = None
        for value in reversed(array):
            self.head = Node(value, self.head)

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

        return ' -> '.join([*result_list, str(None)])

    def __len__(self):
        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            count += 1

        return count

    def pushleft(self, value):
        self.head = Node(value, self.head)

    def popleft(self):
        if self.head is None:
            raise ValueError("Cannot pop from empty list")

        result = self.head.data
        self.head = self.head.next
        return result

    def popright(self):
        if self.head is None:
            raise IndexError('Index out of range')

        if self.head.next is None:
            result = self.head.data
            self.head = None
            return result

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        result = temp.next.data
        temp.next = None
        return result

    def pushright(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = Node(value)

    def insert(self, value, i):
        temp = self.head
        last = temp
        for _ in range(i):
            if temp is None:
                raise IndexError('Index out of range')
            last = temp
            temp = temp.next

        if i == 0:
            self.head = Node(value, self.head)
        else:
            last.next = Node(value, last.next)

    def delete(self, i):
        if self.head is None:
            raise IndexError('Index out of range')

        if i == 0:
            self.popleft()
            return

        temp = self.head
        for _ in range(i - 1):
            temp = temp.next
            if temp is None or temp.next is None:
                raise IndexError('Index out of range')

        temp.next = temp.next.next


if __name__ == "__main__":
    array = list(range(5))
    ll = LinkedList(array)
    print(ll)

    ll.pushleft(10)
    ll.pushleft(20)
    print(ll)

    ll.pushright(30)
    print(ll)

    print(ll.popleft())
    print(ll.popright())
    print(ll)

    ll.delete(0)
    ll.delete(1)
    ll.delete(len(ll) - 1)
    ll.insert(42, 0)
    ll.insert(11, 4)
    print(ll)
