import tkinter as tk

class Node:
    def __init__(self, item = 1, nxt=None):
        self.item = item
        self.next = nxt


class ListaSE(tk.Tk):
    def __init__(self, *args: Node):


        super(ListaSE, self).__init__()
        self.x = 150
        self.y = 220
        self.title("Lista Simplesmente Encadeada")
        self.canvas = tk.Canvas(self, bg="white")
        framelistaSE = tk.Frame(self)


        btn = tk.Button(framelistaSE, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.config(command=self.insert)

        btn2 = tk.Button(framelistaSE, text='delete')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn2.config(command=self.delete)

        btn3 = tk.Button(framelistaSE, text='delete all')
        btn3.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn3.config(command=self.clear)

        self.canvas.pack()
        framelistaSE.pack(fill=tk.BOTH)

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
        a = None
        while p:
            if p.item == v:
                return p, a
            a = p
            p = p.next
        return None

    def insert(self, item = "1"):
        new_node = Node(item, self.head)
        if not self.isEmpty():
            self.head.prev = new_node
        self.head = new_node
        return new_node

    def delete(self, val):
        p, a = self.search(val)
        if not p:
            return False

        if self.head == p:
            self.head = p.next

        if p.next:
            a.next = p.next
        del p
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
        a = None
        while h:
            r = "[" if h == self.head else r + ", "
            if h.next is not None:
                a = str(h.next.item)
            r += str(h.item) + '(' + a + ')'
            h = h.next
        return r + "]"

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x + 30, self.y + 20))
        self.canvas.itemconfig(text_id, text=i)
    
    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.y -= 40
        self.canvas.create_rectangle(box)
        line = (self.x, self.y, self.x+80, self.y)
        self.canvas.create_line(line,arrow=tk.LAST,fill="black",width=2)
        box2 = (self.x, self.y, self.x, self.y)
        self.write_text("prox")
        self.canvas.create_rectangle(box2)

if __name__ == "__main__":
    pass
