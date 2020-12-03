import tkinter as tk
from tkinter import messagebox


class Fila(tk.Toplevel):

    def __init__(self):
        super(Fila, self).__init__()
        self.vet = [1, 2, 3]
        print('Objeto Fila com ', self.vet, ' de valor inicial')
        self.title("Fila")
        self.x = 150
        self.y = 50
        self.canvas = tk.Canvas(self, bg="white")
        framefila = tk.Frame(self)

        self.canvas.bind("<Button-1>", self.error)

        self.var = tk.StringVar()
        labl = tk.Label(framefila, text="Insert: ")
        labl.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.entry = tk.Entry(framefila, width=10, textvariable=self.var)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        btn = tk.Button(framefila, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn.config(command=self.append)

        btn2 = tk.Button(framefila, text='pop')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.X)
        btn2.config(command=self.pop)

        for a in range(len(self.vet)):
            self.draw_quad()
            self.write_text(a)
            self.canvas.pack()
            framefila.pack(fill=tk.BOTH)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x + 30, self.y-60))
        self.canvas.itemconfig(text_id, text=self.vet[i])

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.y += 40
        self.canvas.create_rectangle(box)

    @staticmethod
    def error(event):
        messagebox.showerror("Error", "Movimentação Não permitida pela estrutura")

    def __len__(self):
        return len(self.vet)

    def append(self):
        other = self.var.get()
        if other == '':
            return False
        self.vet.append(other)
        print('Fila: ', self.vet)
        self.draw_quad()
        self.write_text(-1)
        self.entry.delete(0, 'end')
        return other

    def pop(self):
        popped = self.vet.pop(0)
        self.y -= 40 * (len(self.vet) + 1)
        self.canvas.delete(tk.ALL)
        print('Fila: ', self.vet)
        if self.vet:
            for i in range(len(self.vet)):
                self.draw_quad()
                self.write_text(i)
            return popped
        else:
            return False


if __name__ == "__main__":
    app = Fila()
    app.mainloop()
