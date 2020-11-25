class BranchLeaf:
    def __init__(self, item, right=None, left=None):
        self.item = item
        self.right = right
        self.left = left


class BinaryTree:

    def __init__(self, height=0):
        self.head = None
        self.height = height

    def __str__(self):
        return self.__print_structure()

    def __print_structure(self, root='['):
        if self.head is not None:
            if root[-1] == ']' and self.head.left and self.head.right is not None:
                root += '['
            root += str(self.head.item)+'('+str(self.height)+')' + ']'
            if self.head.left is not None:
                root = self.head.left.__print_structure(root)
            if self.head.left is not None:
                root = self.head.right.__print_structure(root)
        return root

    def insert(self, item):
        root = self.head
        new = BranchLeaf(item)

        if root is None:
            self.head = new
            self.head.left = BinaryTree(self.height+1)
            self.head.right = BinaryTree(self.height+1)

        elif item < root.item:
            self.head.left.insert(item)

        elif item > root.item:
            self.head.right.insert(item)

    # not working properly
    def remove(self, item):
        if self.head is not None:

            if self.head.item is item:
                r_item = self.head
                if self.head.left.head is None:
                    self.head = self.head.right.head

                elif self.head.right.head is None:
                    self.head = self.head.left.head

                else:
                    self.head = self.head.right.head

                del r_item
                return

            elif item <= self.head.item:
                self.head.left.remove(item)

            elif item >= self.head.item:
                self.head.right.remove(item)

        else:
            return False

    def search(self, item):
        if self.head is not None:

            if self.head.item is item:
                print('Found [', item, '] at level (', self.height, ')')
                return

            elif item <= self.head.item:
                self.head.left.search(item)

            elif item >= self.head.item:
                self.head.right.search(item)

        else:
            return


if __name__ == "__main__":
    arvore = BinaryTree()
    arvore.insert(5)
    arvore.insert(2)
    arvore.insert(3)
    arvore.insert(7)
    arvore.insert(8)
    arvore.insert(9)
    print(arvore.search(8))
    print(arvore)
    arvore.remove(7)
    print(arvore)
