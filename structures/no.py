import tkinter as tk


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
    def __init__(self, x=130, y=240, v: list = "1"):
        super().__init__()
        self.title("Pilha")
        self.x = x
        self.y = y
        self.v = v
        self.canvas = tk.Canvas(self, bg="white")
        # frame = tk.Frame(self)
        self.draw_quad()
        self.text_id = self.canvas.create_text((160, 220))
        # self.canvas.bind("<Button-1>", self.draw_quad)
        self.write_text()
        for a in range(len(self.v)):
            self.canvas.pack()

        # self.update()

    def write_text(self):
        self.canvas.itemconfig(self.text_id, text=self.v)

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.canvas.create_rectangle(box)


app = NoQuadrado()
app.mainloop()
