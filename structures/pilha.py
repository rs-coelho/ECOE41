import tkinter as tk


class Pilha(tk.Toplevel):

    def __init__(self):
        super(Pilha, self).__init__()
        self.vet = [1, 2, 3]
        print('Objeto Pilha com ', self.vet, ' de valor inicial')
        self.title("Pilha")
        self.x = 150
        self.y = 260
        self.canvas = tk.Canvas(self, bg="white")
        frame_pilha = tk.Frame(self)

        self.canvas.bind('<Double-1>', self.append_double)

        self.var = tk.StringVar()
        labl = tk.Label(frame_pilha, text="Insert: ")
        labl.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.entry = tk.Entry(frame_pilha, textvariable=self.var)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        btn = tk.Button(frame_pilha, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.config(command=self.append)

        btn2 = tk.Button(frame_pilha, text='pop')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn2.config(command=self.pop)

        for a in range(len(self.vet)):
            self.draw_quad()
            self.write_text(a)
            self.canvas.pack()
            frame_pilha.pack(fill=tk.BOTH)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x + 30, self.y + 20))
        self.canvas.itemconfig(text_id, text=self.vet[i])

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.y -= 40
        self.canvas.create_rectangle(box)

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

    def append_double(self, event):
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
        popped = self.vet.pop()
        self.y += 40 * (len(self.vet) + 1)
        self.canvas.delete(tk.ALL)
        print('Pilha: ', self.vet)
        if self.vet:
            for i in range(len(self.vet)):
                self.draw_quad()
                self.write_text(i)
            return popped
        else:
            return False


if __name__ == "__main__":
    app = Pilha()
    app.mainloop()
    pass
