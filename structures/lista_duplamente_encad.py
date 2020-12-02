import tkinter as tk

class Node(tk.Tk):
    def __init__(self, item, nxt=None, prv=None):
        super(Node, self).__init__()
        self.item = item
        self.next = nxt
        self.prev = prv


class ListaDE(tk.Tk):
    def __init__(self, *args: Node):

        super(ListaDE, self).__init__()
        self.title("Lista Duplamente Encadeada")
        self.canvas = tk.Canvas(self, bg="white")
        framelistaDE = tk.Frame(self)
        self.x = 150
        self.y = 220

        btn = tk.Button(framelistaDE, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.config(command=self.insert)
        
        btn4 = tk.Button(framelistaDE, text='search')
        btn4.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn4.config(command=self.search)

        btn2 = tk.Button(framelistaDE, text='delete')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn2.config(command=self.delete)

        btn3 = tk.Button(framelistaDE, text='delete all')
        btn3.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn3.config(command=self.clear)

        self.canvas.pack()
        framelistaDE.pack(fill=tk.BOTH)

        self.head = None
        for _ in args:
            self.insert(_)
        
    def __str__(self):
        h = self.head
        r = "["
        while h:
            r = "[" if h == self.head else r + ", "
            r += str(h.item)
            h = h.next
        return r + "]"

    def __len__(self):
        p = self.head
        c = 0
        while p:
            c += 1
            p = p.next
        return c

    def isEmpty(self):
        return self.head is None

    def search(self, v):
        if self.isEmpty():
            return None
        p = self.head
        while p:
            if p.item == v:
                return p
            p = p.next
        return None

    def insert(self, item=1):
        new_node = Node(item, self.head)
        if not self.isEmpty():
            self.head.prev = new_node
        self.head = new_node
        print(self.head.item)
        return new_node

    def delete(self, val):
        p = self.search(val)
        if not p:
            return False

        if self.head == p:
            self.head = p.next
        else:
            p.prev.next = p.next

        if p.next:
            p.next.prev = p.prev
        del p
        print(self.head.item)
        return True

    def clear(self):
        p = self.head
        self.head = None
        t = None
        while p:
            t = p.next
            del p
            p = t

    def print_linked(self):
        
        h = self.head
        r = "["
        a, b = None, None
        while h:
            r = "[" if h == self.head else r + ", "
            if h.next is not None:
                a = str(h.next.item)
            if h.prev is not None:
                b = str(h.prev.item)
            r += str(h.item) + '(' + a + ', ' + b + ')'
            h = h.next
        return r + "]"

    def set_selection(self, widget):
        for w in widget.master.winfo_children():
            w.config(relief=tk.RAISED)
            widget.config(relief=tk.SUNKEN)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x + 30, self.y + 20))
        self.canvas.itemconfig(text_id, text=i)
    def draw_quad(self):


        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.y -= 40
        self.canvas.create_rectangle(box)

        box2 = (self.x, self.y, self.x+30, self.y)
        self.write_text("prox")
        self.canvas.create_rectangle(box2)

        box3 = (self.x, self.y, self.x-150, self.y)
        self.write_text("ant")
        self.canvas.create_rectangle(box3)

        line = (self.x, self.y, self.x, self.y)
        self.canvas.create_line(line,arrow=tk.LAST,fill="black",width=2)


if __name__ == "__main__":
    app = ListaDE()
    app.mainloop()
    pass

