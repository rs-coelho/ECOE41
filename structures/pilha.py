import tkinter as tk
from functools import partial
from structures.no import NoRedondo

# A pilha estão seguindo os padrões do exAddingShapes
# Modifique para que ela aceite o NoRedondo


class Pilha(tk.Tk):
    shapes = ("rectangle", "oval", "arc")

    def __init__(self, stuff: list = (1, 2, 3)):
        super(Pilha, self).__init__()
        self.vet = stuff
        print('Objeto Pilha com ', self.vet, ' de valor inicial')
        self.title("Drawing standard items")
        self.start = None
        self.shape = None
        self.canvas = tk.Canvas(self, bg="white")
        frame = tk.Frame(self)
        for shape in self.shapes:
            btn = tk.Button(frame, text=shape.capitalize())
            btn.config(command=partial(self.set_selection, btn, shape))
            btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            self.canvas.bind("<Button-1>", self.draw_item)
            self.canvas.pack()
            frame.pack(fill=tk.BOTH)

    def set_selection(self, widget, shape):
        for w in widget.master.winfo_children():
            w.config(relief=tk.RAISED)
        widget.config(relief=tk.SUNKEN)
        self.shape = shape

    def draw_item(self, event):
        x, y = event.x, event.y
        if not self.start:
            self.start = (x, y)
        else:
            x_origin, y_origin = self.start
            self.start = None
            bbox = (x_origin, y_origin, x, y)
            if self.shape == "rectangle":
                self.canvas.create_rectangle(*bbox, fill="blue", activefill="yellow")
            elif self.shape == "oval":
                self.canvas.create_oval(*bbox, fill="red", activefill="yellow")
            elif self.shape == "arc":
                self.canvas.create_arc(*bbox, fill="green", activefill="yellow")

    def __len__(self):
        return len(self.vet)

    def append(self, other):
        self.vet.append(other)

    def pop(self):
        return self.vet.pop()
