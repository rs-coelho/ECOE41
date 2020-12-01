from structures.pilha import Pilha
from structures.fila import Fila
import tkinter as tk


class Execute(tk.Tk):

    def __init__(self):
        super(Execute, self).__init__()
        print('Main Menu initiated')
        self.title("Main Menu")
        self.geometry('350x275')

        btn = tk.Button(self, text='Pilha')
        btn.config(command=Pilha)
        btn.grid(row=1, column=1)

        btn2 = tk.Button(self, text='Fila')
        btn2.config(command=Fila)
        btn2.grid(row=1, column=3)

    def run(self):
        self.mainloop()
        # p = Pilha()
        # p.mainloop()


if __name__ == '__main__':
    print('Log Begin')
    print('------------------------------------')
    ex = Execute()
    ex.run()
    print('------------------------------------')
    print('Log End')
