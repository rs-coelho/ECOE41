import tkinter as tk


class Node:
    def __init__(self, item=1):
        self.item = item
        self.next = None


class ListaSE(tk.Toplevel):
    def __init__(self):

        super(ListaSE, self).__init__()
        self.len = 0
        self.title("Lista Simplesmente Encadeada")
        self.canvas = tk.Canvas(self, bg="white")
        framelista_se = tk.Frame(self)
        self.x = 30
        self.y = 220

        self.canvas.bind("<Button-1>", self.drag_start)
        self.canvas.bind("<B1-Motion>", self.drag_motion)

        self.var = tk.StringVar()
        labl = tk.Label(framelista_se, text="Insert: ")
        labl.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.entry = tk.Entry(framelista_se, width=10, textvariable=self.var)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        btn = tk.Button(framelista_se, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn.config(command=self.insert)

        btn2 = tk.Button(framelista_se, text='delete')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn2.config(command=self.delete)

        btn3 = tk.Button(framelista_se, text='clear')
        btn3.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn3.config(command=self.clear)

        self.canvas.pack()
        framelista_se.pack(fill=tk.BOTH)

        self.head = None

    def __str__(self):
        h = self.head
        r = "["
        while h:
            r = "[" if h == self.head else r + ", "
            r += str(h.item)
            if h.next is not None:
                a = str(h.next.item)
                r += '(' + a + ')'
            else:
                r += '(None)'
            h = h.next
        return r + "]"

    def isEmpty(self):
        return self.head is None

    def search(self, v):
        if self.isEmpty():
            return None
        p = self.head
        a = None
        while p:
            if p.item == v:
                return p, a
            a = p
            p = p.next
        return None

    # Terminal ok | Canvas ok
    def insert(self):
        item = self.var.get()
        self.entry.delete(0, 'end')
        if item == '':
            return False
        self.len += 1
        new_node = Node(item)
        k = self.head
        if not self.isEmpty():
            while k.next is not None:
                k = k.next
            k.next = new_node
        else:
            self.head = new_node
        self.draw_quad()
        self.write_text(item)
        print('ListaSE: ', self)
        return new_node

    # Terminal ok | Canvas ok
    def delete(self):
        val = self.var.get()
        self.entry.delete(0, 'end')
        if val == '':
            return False
        p, a = self.search(val)
        print('Deleting:', p.item)
        if not p:
            return False

        if self.head == p:
            self.head = p.next

        if a is not None:
            a.next = p.next

        del p

        k = self.head
        self.canvas.delete(tk.ALL)
        self.x = 30
        while k:
            self.draw_quad()
            self.write_text(k.item)
            k = k.next
        print('ListaSE: ', self)
        return True

    def clear(self):
        p = self.head
        self.head = None
        while p:
            t = p.next
            del p
            p = t
        self.canvas.delete(tk.ALL)
        self.x = 30
        print('ListaSE: ', self)

    @staticmethod
    def drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def drag_motion(self, event):
        x_item = self.canvas.find_closest(event.x, event.y)
        x = event.x
        y = event.y
        self.canvas.itemconfig(x_item, x=x, y=y)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x - 50, self.y - 20))
        self.canvas.itemconfig(text_id, text=i)

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.canvas.create_rectangle(box)
        line = (self.x + 60, self.y - 20, self.x + 80, self.y - 20)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)
        self.x += 80


if __name__ == "__main__":
    app = ListaSE()
    app.mainloop()
    pass

