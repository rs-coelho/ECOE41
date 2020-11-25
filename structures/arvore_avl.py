class Branch:
    def __init__(self, item, right=None, left=None):
        self.item = item
        self.right = right
        self.left = left


class AVLTree:
    def __init__(self):
        self.head = None
        self.height = -1
        self.balance = 0

    def __str__(self):
        return self.display()

    def display(self, level=0, pref=''):
        if self.head is not None:
            print('-' * level * 2, pref, self.head.item, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.height == 0 else ' ')
            if self.head.left is not None:
                self.head.left.display(level + 1, '<')
            if self.head.left is not None:
                self.head.right.display(level + 1, '>')
        return

    def insert(self, item):
        tree = self.head

        new = Branch(item)

        if tree is None:
            self.head = new
            self.head.left = AVLTree()
            self.head.right = AVLTree()

        elif item < tree.item:
            self.head.left.insert(item)

        elif item > tree.item:
            self.head.right.insert(item)

        self.rebalance()

    def search(self, item):
        if self.head is not None:
            if self.head.item == item:
                return True
            if self.head.left is not None:
                self.head.left.search(item)
            if self.head.left is not None:
                self.head.right.search(item)

        return False

    def rebalance(self):
        self.sum_heights()
        self.sum_balances()

        while self.balance < -1 or self.balance > 1:

            if self.balance > 1:

                if self.head.left.balance < 0:
                    self.head.left.rotate_left()
                    self.sum_heights()
                    self.sum_balances()

                self.rotate_right()
                self.sum_heights()
                self.sum_balances()

            if self.balance < -1:

                if self.head.right.balance > 0:
                    self.head.right.rotate_right()
                    self.sum_heights()
                    self.sum_balances()

                self.rotate_left()
                self.sum_heights()
                self.sum_balances()

    def rotate_right(self):
        h = self.head
        left = self.head.left.head
        right = left.right.head

        self.head = left
        left.right.head = h
        h.left.head = right

    def rotate_left(self):
        h = self.head
        right = self.head.right.head
        left = right.left.head

        self.head = right
        right.left.head = h
        h.right.head = left

    def sum_heights(self, recurse=True):
        if self.head is not None:

            if recurse:

                if self.head.left is not None:
                    self.head.left.sum_heights()

                if self.head.right is not None:
                    self.head.right.sum_heights()

            self.height = max(self.head.left.height, self.head.right.height) + 1

        else:
            self.height = -1

    def sum_balances(self, recurse=True):
        if self.head is not None:

            if recurse:

                if self.head.left is not None:
                    self.head.left.sum_balances()

                if self.head.right is not None:
                    self.head.right.sum_balances()

            self.balance = self.head.left.height - self.head.right.height
        else:
            self.balance = 0

    def remove(self, item):
        if self.head is not None:

            if self.head.item is item:

                if self.head.left.head is None and self.head.right.head is None:
                    self.head = None

                elif self.head.left.head is None:
                    self.head = self.head.right.head

                elif self.head.right.head is None:
                    self.head = self.head.left.head

                self.rebalance()
                return

            elif item < self.head.item:
                self.head.left.remove(item)

            elif item > self.head.item:
                self.head.right.remove(item)

            self.rebalance()
        else:
            return


if __name__ == "__main__":
    arvore = AVLTree()
    arvore.insert(5)
    arvore.insert(2)
    arvore.insert(3)
    arvore.insert(7)
    arvore.insert(8)
    arvore.insert(9)
    print(arvore.search(7))
    print(arvore)
