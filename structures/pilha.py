import tkinter as tk


class Pilha(tk.Tk):

    def __init__(self):
        super(Pilha, self).__init__()
        self.vet = [1, 2, 3]
        print('Objeto Pilha com ', self.vet, ' de valor inicial')
        self.title("Pilha")
        self.x = 150
        self.y = 220
        self.canvas = tk.Canvas(self, bg="white")
        frame_pilha = tk.frame_pilha(self)

        btn = tk.Button(frame_pilha, text='insert')
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.config(command=self.append)
        self.canvas.bind("<Button-1>", self.append(1))

        btn2 = tk.Button(frame_pilha, text='pop')
        btn2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn2.config(command=self.pop)
        self.canvas.bind("<Button-2>", self.pop())

        for a in range(len(self.vet)):
            self.draw_quad()
            self.write_text(a)
            self.canvas.pack()
            frame_pilha.pack(fill=tk.BOTH)

    def set_selection(self, widget):
        for w in widget.master.winfo_children():
            w.config(relief=tk.RAISED)
            widget.config(relief=tk.SUNKEN)

    def write_text(self, i):
        text_id = self.canvas.create_text((self.x + 30, self.y + 20))
        self.canvas.itemconfig(text_id, text=self.vet[i])

    def draw_quad(self):
        box = (self.x, self.y, self.x + 60, self.y - 40)
        self.y -= 40
        self.canvas.create_rectangle(box)

    def __len__(self):
        return len(self.vet)

    def append(self, other=1):
        self.vet.append(other)
        print(self.vet)
        self.draw_quad()
        self.write_text(-1)

    def pop(self):
        self.y += 40 * (len(self.vet) + 1)
        self.canvas.delete(tk.ALL)
        print(self.vet)
        if self.vet:
            for i in range(len(self.vet)):
                self.draw_quad()
                self.write_text(i)
            return self.vet.pop()
        else:
            return


if __name__ == "__main__":
    app = Pilha()
    app.mainloop()
    pass
