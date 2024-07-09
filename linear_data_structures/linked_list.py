class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'Node({self.data}, {self.next})'


class LinkedList:
    def __init__(self, array):
        self.head = None
        for value in array:
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

    def pushleft(self, value):
        self.head = Node(value, self.head)

    def popleft(self):
        pass

    def popright(self):
        pass

    def pushright(self, value):
        pass

    def insert(self, value, i):
        pass

    def delete(self, i):
        pass


if __name__ == "__main__":
    array = list(range(5))
    ll = LinkedList(array)
    print(ll)
    print(ll)

    ll.pushleft(10)
    ll.pushleft(20)
    print(ll)
