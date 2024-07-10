from random import randrange


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node({self.data}, {self.left}, {self.right})'

    def is_leaf(self):
        return self.left is None and self.right is None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def __str__(self):
        return str(self.root)

    def __len__(self):
        return self.count

    def __contains__(self, x):
        return x in (node.data for node in self)
        # Alternative
        # return x in map(lambda node: node.data, self)

    def __iter__(self):
        return self.__iter_tree_rec(self.root)

    @staticmethod
    def __iter_tree_rec(node):
        if node is None:
            return

        yield node
        yield from BinaryTree.__iter_tree_rec(node.left)
        yield from BinaryTree.__iter_tree_rec(node.right)

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
        self.count += 1

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

    def sum(self):
        if self.root is None:
            return 0
        return sum(node.data for node in self)

    def max(self):
        if self.root is None:
            raise ValueError('Tree is empty')
        return max(node.data for node in self)

    def min(self):
        if self.root is None:
            raise ValueError('Tree is empty')
        return min(node.data for node in self)
        # Alternative
        # return min(self, key=lambda x: x.data).data

    @staticmethod
    def __height_rec(node):
        if node is None:
            return 0

        return 1 + max(BinaryTree.__height_rec(node.left), BinaryTree.__height_rec(node.right))

    def height(self):
        if self.root is None:
            return 0
        return self.__height_rec(self.root) - 1

    def width(self):
        if self.root is None:
            return 0

        left = right = self.root
        left_count = right_count = 0
        while left.left is not None:
            left = left.left
            left_count += 1

        while right.right is not None:
            right = right.right
            right_count += 1

        return left_count + right_count

    @staticmethod
    def __width_rec_oneway(node, direction):
        if node is None:
            return -1

        return 1 + BinaryTree.__width_rec_oneway(node.left if direction == 'left' else node.right, direction)
        # Alternativa
        # return 1 + BinaryTree.__width_rec_oneway(getattr(node, direction), direction)

    def width_rec(self):
        if self.root is None:
            return 0

        return self.__width_rec_oneway(self.root, 'left') + self.__width_rec_oneway(self.root, 'right')

    def get_leaves(self):
        return [node.data for node in self if node.is_leaf()]

    def find_parent(self, x):
        return self.find_parent_rec(self.root, x)

    def find_parent_rec(self, node, value):
        if node is None:
            return None

        if node.left is not None and node.left.data == value or node.right is not None and node.right.data == value:
            return node.data

        left_subtree = self.find_parent_rec(node.left, value)
        right_subtree = self.find_parent_rec(node.right, value)

        return left_subtree if left_subtree is not None else right_subtree


def generate_random_tree(n):
    tree = BinaryTree()
    for i in range(n):
        tree.add(i)

    return tree


if __name__ == "__main__":
    tree = generate_random_tree(20)
    print(tree)
    tree.preorder()
    tree.inorder()
    tree.postorder()
    print()
    print('sum', tree.sum())
    print('max', tree.max())
    print('min', tree.min())
    print('len', len(tree))
    print('height', tree.height())
    print('width', tree.width())
    print('width_rec', tree.width_rec())

    print(3 in tree)
    print('parent of 2 is', tree.find_parent(2))
    print(tree.get_leaves())

    # for data in tree:
    #     print(data)
