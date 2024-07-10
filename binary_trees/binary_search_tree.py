from random import randrange

from binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def __contains__(self, x):
        pass

    def add(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        node = self.root
        parent = node
        last_direction = True
        while node is not None:
            parent = node
            if x == node.data:
                return
            elif x < node.data:
                node = node.left
                last_direction = True
            else:
                node = node.right
                last_direction = False

        if last_direction:
            parent.left = Node(x)
        else:
            parent.right = Node(x)


if __name__ == "__main__":
    tree = BinarySearchTree()
    for i in range(6):
        tree.add(randrange(20))

    print(tree)
    tree.preorder()
    tree.inorder()
    tree.postorder()
    print()
    print('sum', tree.sum())
    print('max', tree.max())
    print('min', tree.min())
    print('height', tree.height())
    print('width', tree.width())
    print('width_rec', tree.width_rec())

    print(3 in tree)
    print('parent of 2 is', tree.find_parent(2))
    print(tree.get_leaves())
