from structures.pilha import Pilha
from structures.fila import Fila
from structures.lista_simplesmente_encad import ListaSE
from structures.lista_duplamente_encad import ListaDE
from structures.arvore_binaria import BinaryTreeWindow
from structures.arvore_binaria_busca import BinarySearchTree
import tkinter as tk


class Execute(tk.Tk):

    def __init__(self):
        super(Execute, self).__init__()
        print('############# Main Menu initiated #############')
        self.title("Main Menu")
        padding_x = 5
        padding_y = 5

        msg = \
            '''
----------------------------------------------------------------------------------------
|                                Bem vindo ao menu principal!                            |
|                                                                                                             |
|                                                                                                             |
|Este é um app para ajudar a compreender as estruturas de dados.  |
|Por favor escolha uma das estruturas disponiveis:                            |
|                                                                                                             |
----------------------------------------------------------------------------------------
        '''
        label = tk.Label(self, text=msg)
        label.grid(row=0, columnspan=2, padx=padding_x)

        btn = tk.Button(self, text='Pilha')
        btn.config(command=Pilha)
        btn.grid(row=1, column=0, padx=padding_x, pady=padding_y, sticky='NWSE')

        btn2 = tk.Button(self, text='Fila')
        btn2.config(command=Fila)
        btn2.grid(row=1, column=1, padx=padding_x, pady=padding_y, sticky='NWSE')

        btn3 = tk.Button(self, text='Lista Simples Enc.')
        btn3.config(command=ListaSE)
        btn3.grid(row=2, column=0, padx=padding_x, pady=padding_y, sticky='NWSE')

        btn4 = tk.Button(self, text='Lista Dupla Enc.')
        btn4.config(command=ListaDE)
        btn4.grid(row=2, column=1, padx=padding_x, pady=padding_y, sticky='NWSE')

        btn5 = tk.Button(self, text='Arvore Binaria')
        btn5.config(command=BinaryTreeWindow)
        btn5.grid(row=3, column=0, padx=padding_x, pady=padding_y, sticky='NWSE')

        btn6 = tk.Button(self, text='Arvore Bsc Binaria')
        btn6.config(command=BinarySearchTree)
        btn6.grid(row=3, column=1, padx=padding_x, pady=padding_y, sticky='NWSE')

        msg2 = 'Created by Rodrigo Coelho and Samuel Siqueira'
        label1 = tk.Label(self, text=msg2)
        label1.grid(row=4, columnspan=2, padx=padding_x)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    print('----------------- Log Begin -------------------')
    ex = Execute()
    ex.run()
    print('-----------------  Log End  -------------------')
