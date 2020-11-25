import tkinter as tk


class Fila(tk.Tk):

    def __init__(self, stuff: list = [1, 2, 3]):
        self.vet = stuff
        print('Objeto Pilha com ', self.vet, ' de valor inicial')

    def __len__(self):
        pass

    def append(self, other, pos: int = -1):
        self.vet.append(other)

    def pop(self):
        self.vet.pop(0)


if __name__ == "__main__":
    # write test code
    pass

