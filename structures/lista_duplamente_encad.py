# mudar pois está implementada como uma lista duplamente encadeada

class Node:
    def __init__(self, item, nxt=None, prv=None):
        self.item = item
        self.next = nxt
        self.prev = prv


class ListaDE:
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
        while p:
            if p.item == v:
                return p
            p = p.next
        return None

    def insert(self, item):
        new_node = Node(item, self.head)
        if not self.isEmpty():
            self.head.prev = new_node
        self.head = new_node
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


if __name__ == "__main__":
    # write test code
    pass

