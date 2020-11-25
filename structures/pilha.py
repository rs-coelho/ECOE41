import tkinter as tk
from functools import partial
from structures.no import NoRedondo, NoQuadrado


# A pilha estão seguindo os padrões do exAddingShapes
# Modifique para que ela aceite o NoRedondo


class Pilha(tk.Tk):

    def __init__(self, stuff: list = (1, 2, 3)):
        super(Pilha, self).__init__()
        self.vet = stuff
        print('Objeto Pilha com ', self.vet, ' de valor inicial')
        # self.canvas = tk.Canvas(self, bg="white")
        # self.draw = NoRedondo(160, 230, self.vet[1])

        # self.draw.pack()

    def __len__(self):
        return len(self.vet)

    def append(self, other):
        self.vet.append(other)

    def pop(self):
        return self.vet.pop()


if __name__ == "__main__":
    app = Pilha()
    # app.mainloop()
    pass

