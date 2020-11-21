from structures.pilha import Pilha


class Execute:
    @staticmethod
    def run():
        p = Pilha()
        p.mainloop()


if __name__ == '__main__':
    print('Log Begin')
    print('------------------------------------')
    Execute.run()
    print('------------------------------------')
    print('Log End')
