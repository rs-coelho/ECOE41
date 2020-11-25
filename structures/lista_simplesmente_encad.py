

class Node:
    def __init__(self, item, nxt=None):
        self.item = item
        self.next = nxt


class ListaSE:
    def __init__(self, *args: Node):
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

    def insert(self, item):
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
