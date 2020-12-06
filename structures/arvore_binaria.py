import tkinter as tk


class BranchLeaf:
    def __init__(self, item, right=None, left=None):
        self.item = item
        self.right = right
        self.left = left
        self.r = 3


class BinaryTree(tk.Toplevel):

    def __init__(self, height=0):
        self.head = None
        self.height = height
        if self.height == 0:
            super(BinaryTree, self).__init__()

        self.title("Arvore de busca binaria")
        self.canvas = tk.Canvas(self, bg="white")
        framearv_bus = tk.Frame(self)
        self.x = 150
        self.y = 30
        self.r = 30
        self.xr = 190
        self.yr = 100

        self.var = tk.StringVar()

        labl = tk.Label(framearv_bus, text="Insert: ")
        labl.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.entry = tk.Entry(framearv_bus, width=10, textvariable=self.var)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        btn = tk.Button(framearv_bus, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn.config(command=self.insert)

        btn2 = tk.Button(framearv_bus, text='delete')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn2.config(command=self.remove)

        self.canvas.pack()
        framearv_bus.pack(fill=tk.BOTH)

    def __str__(self):
        return self.__print_structure()

    def __print_structure(self, root='['):
        if self.head is not None:
            if root[-1] == ']' and self.head.left and self.head.right is not None:
                root += '['
            root += str(self.head.item) + '(' + str(self.height) + ')' + ']'
            if self.head.left is not None:
                root = self.head.left.__print_structure(root)
            if self.head.left is not None:
                root = self.head.right.__print_structure(root)
        return root

    def insert(self, item=None):
        if item is None:
            item = self.var.get()
            self.entry.delete(0, 'end')
            if item == '':
                return False
        root = self.head
        new = BranchLeaf(item)

        if item == '':
            return False

        if root is None:
            self.head = new
            print(" ak")
            self.write_text(item)
            self.draw_circle()
            self.head.left = BinaryTree(self.height + 1)
            self.head.right = BinaryTree(self.height + 1)

        if item < root.item and root.right is None:

            print("passou aki")
            self.write_text(item)
            self.draw_circle_left()
        elif root.right is not None:
            self.head.left.insert(item)

        if item > root.item and root.right is None:

            print("passou aki2")
            self.write_text_right(item)
            self.draw_circle_right()
        elif root.left is not None:
            self.head.right.insert(item)

        # not working properly

    def remove(self, item=None):
        if item is None:
            item = self.var.get()
            self.entry.delete(0, 'end')
            if item == '':
                return False

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

            elif item <= self.head.item and self.head.left is not None:
                self.head.left.remove(item)

            elif item >= self.head.item and self.head.right is not None:
                self.head.right.remove(item)

        else:
            return False

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x, self.y))
        self.canvas.itemconfig(text_id, text=i)

    def write_text_right(self, i):
        text_id = self.canvas.create_text((self.xr, self.yr))
        self.canvas.itemconfig(text_id, text=i)

    def draw_circle(self):  # x=130, y=30, r=30
        circle = (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.canvas.create_oval(circle)

        line = ((self.x - self.r) + 10, (self.y - self.r) + 50, (self.x + self.r) - 75, (self.y + self.r) + 15)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)

        line = ((self.x - self.r) + 52, (self.y - self.r) + 50, (self.x + self.r) + 17, (self.y + self.r) + 15)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)
        self.x -= 70
        self.y += 60

    def draw_circle_right(self):  # x=130, y=30, r=30
        circle = (self.xr - self.r, self.yr - self.r, self.xr + self.r, self.yr + self.r)
        self.canvas.create_oval(circle)

        line = ((self.xr - self.r) + 10, (self.yr - self.r) + 50, (self.xr + self.r) - 75, (self.yr + self.r) + 15)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)

        line = ((self.xr - self.r) + 52, (self.yr - self.r) + 50, (self.xr + self.r) + 17, (self.yr + self.r) + 15)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)

        self.xr += 60
        self.yr += 70

    def draw_circle_left(self):  # x=130, y=30, r=30
        circle = (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.canvas.create_oval(circle)

        line = ((self.x - self.r) + 10, (self.y - self.r) + 50, (self.x + self.r) - 75, (self.y + self.r) + 15)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)

        line = ((self.x - self.r) + 52, (self.y - self.r) + 50, (self.x + self.r) + 17, (self.y + self.r) + 15)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)

        self.x -= 70
        self.y += 60


if __name__ == "__main__":
    arvore = BinaryTree()
    arvore.mainloop()
