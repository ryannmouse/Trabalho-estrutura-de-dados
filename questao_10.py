class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

class DequeDinamica:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def deque_e_vazia(self):
        return self.inicio is None

    def insere_inicio_deque(self, valor):
        novo_no = No(valor)
        if self.deque_e_vazia():
            self.inicio = self.fim = novo_no 
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no

    def insere_final_deque(self, valor):
        novo_no = No(valor)
        if self.deque_e_vazia():
            self.inicio = self.fim = novo_no 
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no

    def remove_inicio_deque(self):
        if self.deque_e_vazia():
            raise IndexError("Deque está vazio!")
        valor = self.inicio.valor
        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        return valor

    def remove_final_deque(self):
        if self.deque_e_vazia():
            raise IndexError("Deque está vazio!")
        valor = self.fim.valor
        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        return valor

    def imprimir(self):
        if self.deque_e_vazia():
            print("Deque está vazio!")
            return
        atual = self.inicio
        while atual:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()