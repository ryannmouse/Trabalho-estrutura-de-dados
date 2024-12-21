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
        
    def deque_e_vazia(self): ## Complexidade O(1)
        return self.inicio is None

    def insere_inicio_deque(self, valor): ## Complexidade O(1)
        '''Insere um valor no inicio da Deque'''
        newest = Node(valor)
        if self.deque_e_vazia():
            self.inicio = self.fim = newest  ## Caso seja o primeiro valor inserido, define fim e inicio como newest  
        else:
            newest.proximo = self.inicio ## Caso contrario, insere no inicio e define o novo nó como inicio
            self.inicio.anterior = newest   
            self.inicio = newest            

    def insere_final_deque(self, valor):    ## Complexidade O(1)
        '''Insere um valor no final da Deque'''
        newest = Node(valor)
        if self.deque_e_vazia():
            self.inicio = self.fim = newest ## Caso seja o primeiro valor inserido, define fim e inicio como newest
        else:
            newest.anterior = self.fim ## Caso contrario, insere no final e define o novo nó como final
            self.fim.proximo = newest       
            self.fim = newest              

    def remove_inicio_deque(self): ## Complexidade O(1)
        '''Remove primeiro valor da Deque'''
        if self.deque_e_vazia():
            raise IndexError("Deque está vazio!")
        valor = self.inicio.valor            
        if self.inicio == self.fim:          
            self.inicio = self.fim = None ## Caso haja apenas um único valor, a deque se torna vazia
        else:
            self.inicio = self.inicio.proximo  ## Caso contrario, remove do inicio e define o próximo como inicio
            self.inicio.anterior = None        
        return valor

    def remove_final_deque(self): ## Complexidade O(1)
        '''Remove ultimo valor da Deque'''
        if self.deque_e_vazia():
            raise IndexError("Deque está vazio!")
        valor = self.fim.valor            
        if self.inicio == self.fim:          
            self.inicio = self.fim = None ## Caso haja apenas um único valor, a deque se torna vazia
        else:
            self.fim = self.fim.anterior ## Caso contrario, remove do final e define o anterior como final
            self.fim.proximo = None          
        return valor

    def imprimir(self): ## Complexidade O(n)
        '''Imprime os valores da deque'''
        if self.deque_e_vazia():
            print("Deque está vazio!") ## Caso a deque esteja vazia, imprime uma mesagem
            return
        atual = self.inicio
        while atual:
            print(atual.valor, end=" ") ## Caso contrario, imprime todos os valores da lista
            atual = atual.proximo
        print()


###### TESTE ######

if __name__ == "__main__":
    deque = DequeDinamica()
    print("Deque está vazio:", deque.deque_e_vazia())  # Deve retornar True
    print()
    
    print("Inserindo elementos no inicio da Deque...")
    deque.insere_inicio_deque(10)  # Inserindo o primeiro elemento
    deque.insere_inicio_deque(20)  # Adicionando no inicio
    deque.insere_inicio_deque(30)  # Adicionando no inicio
    deque.imprimir()  # Imprime a lista atual
    print()
    
    print("Inserindo elementos no final da Deque...")
    deque.insere_final_deque(40)  # Adicionando no final
    deque.insere_final_deque(50)  # Adicionando no final
    deque.insere_final_deque(60)  # Adicionando no final
    deque.imprimir()  # Imprime a lista atual
    print()
    
    print("Removendo elementos do inicio da Deque...")
    deque.remove_inicio_deque()  # Removendo do inicio
    deque.remove_inicio_deque()  # Removendo do inicio
    deque.imprimir()  # Imprime a lista atual
    print()
    
    print("Removendo elementos do final da Deque...")
    deque.remove_final_deque()  # Removendo do final
    deque.remove_final_deque()  # Removendo do final
    deque.imprimir()  # Imprime a lista atual
    print()
    
    print("Deque está vazio:", deque.deque_e_vazia())  # Deve retornar True
    print()