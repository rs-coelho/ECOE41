class Branch:
    def __init__(self, item, right=None, left=None):
        self.item = item
        self.right = right
        self.left = left


class AVLTree:
    def __init__(self, head: Branch):
        self.head = head
        self.height = -1
        self.balance = 0

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

    def rebalance(self):
        self.sum_heights(False)
        self.sum_balances(False)

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
        l = self.head.left.head
        r = l.right.head

        self.head = l
        l.right.head = h
        h.left.head = r

    def rotate_left(self):
        h = self.head
        r = self.head.right.head
        l = r.left.head

        self.head = r
        r.left.head = h
        h.right.head = l

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
                self.head.left.delete(item)

            elif item > self.head.item:
                self.head.right.delete(item)

            self.rebalance()
        else:
            return
