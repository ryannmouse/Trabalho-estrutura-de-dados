class Node:
    
    def __init__(self, valor):
        '''Função para criar o nó'''
        self.valor = valor        
        self.anterior = None     
        self.proximo = None       

class DequeDinamica:
    def __init__(self):
        '''Inicializa Deque'''
        self.inicio = None  
        self.fim = None     
        
    def deque_e_vazia(self):
        return self.inicio is None

    def insere_inicio_deque(self, valor):
        '''Função inserir no inicio'''
        newest = Node(valor)
        if self.deque_e_vazia():
            self.inicio = self.fim = newest  ## Caso seja o primeiro valor inserido, define fim e inicio como newest  
        else:
            newest.proximo = self.inicio ## Caso contrario, insere no inicio e define o novo nó como inicio
            self.inicio.anterior = newest   
            self.inicio = newest            

    def insere_final_deque(self, valor):
        newest = Node(valor)
        if self.deque_e_vazia():
            self.inicio = self.fim = newest ## Caso seja o primeiro valor inserido, define fim e inicio como newest
        else:
            newest.anterior = self.fim ## Caso contrario, insere no final e define o novo nó como final
            self.fim.proximo = newest       
            self.fim = newest              

    def remove_inicio_deque(self):
        if self.deque_e_vazia():
            raise IndexError("Deque está vazio!")
        valor = self.inicio.valor            
        if self.inicio == self.fim:          
            self.inicio = self.fim = None ## Caso haja apenas um único valor, a lista se torna vazia
        else:
            self.inicio = self.inicio.proximo  ## Caso contrario, remove do inicio e define o próximo como inicio
            self.inicio.anterior = None        
        return valor

    def remove_final_deque(self):
        if self.deque_e_vazia():
            raise IndexError("Deque está vazio!")
        valor = self.fim.valor            
        if self.inicio == self.fim:          
            self.inicio = self.fim = None ## Caso haja apenas um único valor, a lista se torna vazia
        else:
            self.fim = self.fim.anterior ## Caso contrario, remove do final e define o anterior como final
            self.fim.proximo = None          
        return valor

    def imprimir(self):
        if self.deque_e_vazia():
            print("Deque está vazio!") ## Caso a deque esteja vazia, imprime uma mesagem
            return
        atual = self.inicio
        while atual:
            print(atual.valor, end=" ") ## Caso contrario, imprime todos os valores da lista
            atual = atual.proximo
        print()
