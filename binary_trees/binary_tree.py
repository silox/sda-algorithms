from random import randrange


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node({self.data}, {self.left}, {self.right})'


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def __str__(self):
        return str(self.root)

    def add(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        temp = self.root
        last = temp
        last_side = True
        while temp is not None:
            last = temp
            if randrange(2):
                temp = temp.left
                last_side = True
            else:
                temp = temp.right
                last_side = False

        if last_side:
            last.left = Node(x)
        else:
            last.right = Node(x)

    @staticmethod
    def __preorder_rec(node):
        if node is None:
            return

        print(node.data, end=' ')
        BinaryTree.__preorder_rec(node.left)
        BinaryTree.__preorder_rec(node.right)

    def preorder(self):
        self.__preorder_rec(self.root)
        print()

    @staticmethod
    def __inorder_rec(node):
        if node is None:
            return

        BinaryTree.__inorder_rec(node.left)
        print(node.data, end=' ')
        BinaryTree.__inorder_rec(node.right)

    def inorder(self):
        self.__inorder_rec(self.root)
        print()

    @staticmethod
    def __postorder_rec(node):
        if node is None:
            return

        BinaryTree.__postorder_rec(node.left)
        BinaryTree.__postorder_rec(node.right)
        print(node.data, end=' ')

    def postorder(self):
        self.__postorder_rec(self.root)
        print()

    @staticmethod
    def __sum_rec(node):
        if node is None:
            return 0
        return node.data + BinaryTree.__sum_rec(node.left) + BinaryTree.__sum_rec(node.right)

    def sum(self):
        return self.__sum_rec(self.root)

    def max(self):
        pass

    def min(self):
        pass

    def height(self):
        # vrati hlbku stromu
        pass

    def width(self):
        # vrati sirku stromu
        pass


def generate_random_tree(n):
    tree = BinaryTree()
    for i in range(n):
        tree.add(i)

    return tree


if __name__ == "__main__":
    tree = generate_random_tree(10)
    print(tree)
    tree.preorder()
    tree.inorder()
    tree.postorder()
    print(tree.sum())
