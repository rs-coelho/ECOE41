from structures.pilha import Pilha
from structures.fila import Fila
from structures.lista_simplesmente_encad import ListaSE
from structures.lista_duplamente_encad import ListaDE
from structures.arvore_binaria import BinaryTree
from structures.arvore_binaria_busca import BinarySearchTree
import tkinter as tk


class Execute(tk.Tk):

    def __init__(self):
        super(Execute, self).__init__()
        print('###### Main Menu initiated ######')
        self.title("Main Menu")
        padding_x = 60
        padding_y = 30

        btn = tk.Button(self, text='Pilha')
        btn.config(command=Pilha)
        btn.grid(row=1, column=1, padx=padding_x, pady=padding_y)

        btn2 = tk.Button(self, text='Fila')
        btn2.config(command=Fila)
        btn2.grid(row=1, column=3, padx=padding_x, pady=padding_y)

        btn3 = tk.Button(self, text='Lista Simples Enc.')
        btn3.config(command=ListaSE)
        btn3.grid(row=2, column=1, padx=padding_x, pady=padding_y)

        btn4 = tk.Button(self, text='Lista Dupla Enc.')
        btn4.config(command=ListaDE)
        btn4.grid(row=2, column=3, padx=padding_x, pady=padding_y)

        btn5 = tk.Button(self, text='Arvore Binaria')
        btn5.config(command=BinaryTree)
        btn5.grid(row=3, column=1, padx=padding_x, pady=padding_y)

        btn6 = tk.Button(self, text='Arvore Binaria de Busca')
        btn6.config(command=BinarySearchTree)
        btn6.grid(row=3, column=3, padx=padding_x, pady=padding_y)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    print('----------------- Log Begin -------------------')
    ex = Execute()
    ex.run()
    print('-----------------  Log End  -------------------')
