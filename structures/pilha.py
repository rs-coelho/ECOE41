class Pilha:
    def __init__(self, *stuff):
        self.vet = [stuff]

    def __len__(self):
        return len(self.vet)

    def append(self, other):
        self.vet.append(other)

    def pop(self):
        return self.vet.pop()
