import tkinter as tk
from tkinter import *
# reference: https://www.educba.com/tkinter-messagebox/

# difficult to use, there fore deprecated


class Input(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Input")
        self.var = tk.StringVar()
        labl = Label(self, text="Insert: ")
        labl.grid(column=0, row=0)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.entry.grid(column=1, row=0)
        self.update()
        self.input = None

        btn = tk.Button(self, text='Ok')
        btn.config(command=self.get_text)
        btn.grid(column=2, row=0)

    def get_text(self, *args):
        print(self.var.get())
        self.input = self.var.get()

    def mainloop(self, n=0):
        super(Input, self).mainloop()
        return self.input


if __name__ == "__main__":
    app = Input()
    app.mainloop()
