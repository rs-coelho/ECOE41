import tkinter as tk


class Node:
    def __init__(self, item, nxt=None, prv=None):
        self.item = item
        self.next = nxt
        self.prev = prv


class ListaDE(tk.Toplevel):
    def __init__(self):

        super(ListaDE, self).__init__()
        self.len = 0
        self.title("Lista Duplamente Encadeada")
        self.canvas = tk.Canvas(self, bg="white")
        framelista_de = tk.Frame(self)
        self.x = 150
        self.y = 220

        self.var = tk.StringVar()
        labl = tk.Label(framelista_de, text="Insert: ")
        labl.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.entry = tk.Entry(framelista_de, width=10, textvariable=self.var)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        btn = tk.Button(framelista_de, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn.config(command=self.insert)
        
        btn4 = tk.Button(framelista_de, text='search')
        btn4.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn4.config(command=self.search)

        btn2 = tk.Button(framelista_de, text='delete')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn2.config(command=self.delete)

        btn3 = tk.Button(framelista_de, text='delete all')
        btn3.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn3.config(command=self.clear)

        self.canvas.pack()
        framelista_de.pack(fill=tk.BOTH)

        self.head = None
        
    def __str__(self):
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

    def insert(self):
        item = self.var.get()
        self.entry.delete(0, 'end')
        if item == '':
            return False
        self.len += 1
        new_node = Node(item, self.head)
        if not self.isEmpty():
            self.head.prev = new_node
        else:
            self.head = new_node
        self.draw_quad()
        self.write_text(item)
        print(self.head.item)
        return new_node

    def delete(self):
        val = self.var.get()
        self.entry.delete(0, 'end')
        if val == '':
            return False
        p, a = self.search(val)
        if self.head == p:
            self.head = p.next
        else:
            p.prev.next = p.next

        if p.next:
            p.next.prev = p.prev
        del p

        k = self.head
        self.canvas.delete(tk.ALL)
        self.x = 150
        while k:
            self.draw_quad()
            self.write_text(k.item)
            k = k.next
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

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x - 50, self.y - 20))
        self.canvas.itemconfig(text_id, text=i)

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.canvas.create_rectangle(box)
        line = (self.x + 60, self.y - 20, self.x + 80, self.y - 20)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)
        line = (self.x, self.y - 20, self.x - 20, self.y - 20)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)
        self.x += 80


if __name__ == "__main__":
    app = ListaDE()
    app.mainloop()
    pass

