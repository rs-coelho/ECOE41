import tkinter as tk


class BranchLeaf:
    def __init__(self, item, right=None, left=None):
        self.item = item
        self.right = right
        self.left = left
        self.r = 3


class BinaryTree(tk.Toplevel):

    def __init__(self):
        super(BinaryTree, self).__init__()
        self.head = None
        self.hght = 0
        print('Objeto Arvore Binaria com ', self, ' de valor inicial')
        self.title("Arvore Binaria")
        self.canvas = tk.Canvas(self, bg="white")
        framebt = tk.Frame(self)
        self.x = 150
        self.y = 100
        self.r = 30

        btn = tk.Button(framebt, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.config(command=self.insert)

        btn2 = tk.Button(framebt, text='remove')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn2.config(command=self.remove)

        self.canvas.pack()
        framebt.pack(fill=tk.BOTH)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x + 30, self.y - 60))
        self.canvas.itemconfig(text_id, text=i)

    def draw_circle(self, x=130, y=220):
        circle = (x - self.r, y - self.r, x + self.r, y + self.r)
        self.canvas.create_oval(circle)

    def __len__(self):
        pass

    def __str__(self):
        return self.__print_structure()

    def __print_structure(self, root='['):
        if self.head is not None:
            if root[-1] == ']' and self.head.left and self.head.right is not None:
                root += '['
            root += str(self.head.item)+'('+str(self.hght)+')' + ']'
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
            self.head.left = BinaryTree(self.hght+1)
            self.head.right = BinaryTree(self.hght+1)

        elif item < root.item:
            self.head.left.insert(item)

        elif item > root.item:
            self.head.right.insert(item)
        self.draw_circle()
        self.write_text(item)

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

            elif item < self.head.item:
                self.head.left.remove(item)

            elif item > self.head.item:
                self.head.right.remove(item)

        else:
            return False


if __name__ == "__main__":
    app = BinaryTree()
    app.mainloop()
    pass
