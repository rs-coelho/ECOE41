import tkinter as tk


class BinaryTree:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def insert(self, obj, item):
        if self.item == item:
            return False

        if item < self.item:
            if self.left:
                self.left.insert(obj, item)
            else:
                self.left = BinaryTree(item)
                print('Inseting: ' + item)
                obj.write_text(item)
                obj.draw_circle_left()

        else:
            if self.right:
                self.right.insert(obj, item)
            else:
                self.right = BinaryTree(item)
                print('Inseting: ' + item)
                obj.write_text_right(item)
                obj.draw_circle_right()

    def print_ordem(self, obj):
        if self.left:
            self.left.print_ordem(obj)
        else:
            obj.write_text(self.item)
            obj.draw_circle_left()

        if self.right:
            self.right.print_ordem(obj)
        else:
            obj.write_text_right(self.item)
            obj.draw_circle_right()


class BinaryTreeWindow(tk.Toplevel):

    def __init__(self):
        super(BinaryTreeWindow, self).__init__()
        self.title("Arvore de busca binaria")
        self.canvas = tk.Canvas(self, bg="white")
        framearv_bus = tk.Frame(self)
        self.tree = None
        self.x = 130
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

    # def __str__(self):
    #     return self.__print_structure()
    #
    # def __print_structure(self, root='['):
    #     if self.tree.item is not None:
    #         if root[-1] == ']' and self.tree.left and self.tree.left is not None:
    #             root += '['
    #         root += str(self.tree.item) + ']'
    #         if self.tree.left is not None:
    #             root = self.tree.left.__print_structure(root)
    #         if self.tree.left is not None:
    #             root = self.tree.left.__print_structure(root)
    #     return root

    def insert(self, item=None):
        if item is None:
            item = self.var.get()
            self.entry.delete(0, 'end')
            if item == '':
                return False

        print('ok1')
        if self.tree is None:
            self.tree = BinaryTree(item)
            self.write_text(item)
            self.draw_circle()

        print('ok2')
        if item == '' or item == self.tree.item:
            return False

        self.tree.insert(self, item)

        # not working properly

    def remove(self, item=None):
        if item is None:
            item = self.var.get()
            self.entry.delete(0, 'end')
            if item == '':
                return False

        if self.tree is not None:

            if self.tree.item is item:
                r_item = self.tree
                if self.tree.left.item is None:
                    self.tree = self.tree.left.item

                elif self.tree.left.item is None:
                    self.tree = self.tree.left.item

                else:
                    self.tree = self.tree.left.item

                del r_item
                return

            elif item <= self.tree.item and self.tree.left is not None:
                self.tree.left.remove(item)

            elif item >= self.tree.item and self.tree.left is not None:
                self.tree.left.remove(item)
        else:
            return False

        self.x = 130
        self.y = 30
        self.r = 30
        self.xr = 190
        self.yr = 100
        self.canvas.delete(tk.ALL)
        self.tree.print_ordem(self)





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
    arvore = BinaryTreeWindow()
    arvore.mainloop()
