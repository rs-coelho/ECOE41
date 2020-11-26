import tkinter as tk
from functools import partial
# considerando as operações possivelmente esta classe não será utilizada

class NoRedondo(tk.Tk):
    def __init__(self, x=130, y=220, r=30, v="1"):
        super().__init__()
        self.x = x
        self.y = y
        self.r = r
        self.v = v
        self.canvas = tk.Canvas(self, bg="white")
        self.draw_circle()
        #  self.canvas.bind("<Double-Button-1>", self.change_var)
        self.text_id = self.canvas.create_text((130, 220))
        self.write_text()
        self.canvas.pack()
        self.update()

    # def change_var(self,event):
    #     self.entry = tk.Entry(self, textvariable=self.var)
    #     self.entry.pack(pady=5)

    def write_text(self):
        self.canvas.itemconfig(self.text_id, text=self.v)
        # self.print()

    def draw_circle(self):
        box = (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.canvas.create_oval(box)


class NoQuadrado(tk.Tk):
    def __init__(self, v: list = ["1", '2', '3']):
        super().__init__()
        self.title("Pilha")
        self.x = 150
        self.y = 240
        self.v = v
        self.canvas = tk.Canvas(self, bg="white")
        frame = tk.Frame(self)
        # self.canvas.bind("<Button-1>", self.draw_quad)
        btn = tk.Button(frame, text='pop')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.config(command=partial(self.set_selection, btn))
        btn2 = tk.Button(frame, text='insert')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn2.config(command=partial(self.set_selection, btn2))
        self.update()
        for a in range(len(self.v)):

            self.canvas.bind("<Button-1>", print('Btn action'))
            frame.pack(fill=tk.BOTH)
            self.canvas.pack()
            self.canvas.pack()
            self.draw_quad()
            print('ok')
            self.write_text(a)

        # self.update()

    def set_selection(self, widget):
        for w in widget.master.winfo_children():
            w.config(relief=tk.RAISED)
        widget.config(relief=tk.SUNKEN)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x + 30, self.y + 20))
        self.canvas.itemconfig(text_id, text=self.v[i])

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.y -= 40
        self.canvas.create_rectangle(box)


if __name__ == "__main__":
    app = NoQuadrado()
    app.mainloop()
    pass


