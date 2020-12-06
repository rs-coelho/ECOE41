import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class ListaDE(tk.Toplevel):
    def __init__(self):

        super(ListaDE, self).__init__()
        self.len = 0
        self.title("Lista Duplamente Encadeada")
        self.canvas = tk.Canvas(self, bg="white")
        framelista_de = tk.Frame(self)
        self.x = 30
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
        r = '['
        a, b = None, None
        while h:
            r = "[" if h == self.head else r + ", "
            if h.next is not None:
                a = str(h.next.item)
            else:
                a = None
            if h.prev is not None:
                b = str(h.prev.item)
            else:
                b = None
            r += '(prv:' + str(b) + ')' + str(h.item) + '(nxt:' + str(a) + ')'
            h = h.next
        return r + "]"

    def isEmpty(self):
        return self.head is None

    def search(self):
        v = self.var.get()
        self.entry.delete(0, 'end')
        if self.isEmpty():
            return None
        p = self.head
        while p:
            if p.item == v:
                print('Found: ', v)
                messagebox.showinfo("Item Found!", "O item " + v + " esta presente na estrutura")
                return p
            p = p.next
        print('Item not found:', v)
        return None

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
            new_node.prev = k
        else:
            self.head = new_node
        self.draw_quad()
        self.write_text(item)
        print('ListaDE: ', self)
        return new_node

    def delete(self):
        val = self.var.get()
        if val == '':
            return False
        p = self.head
        while p.item != val:
            p = p.next
        if self.head == p:
            self.head = p.next
        else:
            p.prev.next = p.next
            if p.next:
                p.next.prev = p.prev
        del p

        k = self.head
        self.canvas.delete(tk.ALL)
        self.x = 30
        while k:
            self.draw_quad()
            self.write_text(k.item)
            k = k.next
        print('ListaDE: ', self)
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
        print('ListaDE: ', self)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x - 50, self.y - 20))
        self.canvas.itemconfig(text_id, text=i)

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.canvas.create_rectangle(box)

        line = (self.x + 60, self.y - 30, self.x + 80, self.y - 30)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)

        line = (self.x, self.y - 10, self.x - 20, self.y - 10)
        self.canvas.create_line(line, arrow=tk.LAST, fill="black", width=2)

        self.x += 80


if __name__ == "__main__":
    app = ListaDE()
    app.mainloop()
    pass
