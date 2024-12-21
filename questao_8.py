class Node:
    '''Node para uma lista duplamente encadeada.'''

    def __init__(self, valor=None, anterior=None, proximo=None):
        self.valor = valor  # Valor armazenado no node
        self.anterior = anterior  # Referência para o nodo anterior
        self.proximo = proximo  # Referência para o próximo nodo


class ListaDuplamenteEncadeada:
    '''Implementação de uma lista duplamente encadeada.''' 

    def __init__(self):  ## Complexidade O(1)
        '''Inicializa uma lista vazia.'''
        self.cabeca = None  # Início da lista
        self.cauda = None  # Final da lista
        self.tamanho = 0  # Número de elementos

    def esta_vazia(self):  ## Complexidade O(1)!
        '''Retorna True se a lista estiver vazia.'''
        return self.tamanho == 0  # Verifica se a lista está vazia
    
    def insert(self, valor, posicao):
        '''Adiciona elemento em determinada posição.'''
        if posicao <= 0:  # Insere no começo da lista
            newest = Node(valor, proximo=self.cabeca)
            self.cabeca.anterior = newest
        elif posicao < self.tamanho: # Insere no meio da lista
            cont = 0
            anterior = self.cabeca
            # Determinando o anterior do newest
            while cont + 1 < posicao:
                anterior = anterior.proximo
            # O proximo do newest será o proximo do anterior
            proximo = anterior.proximo
            newest = Node(valor, anterior, proximo)
            anterior.proximo = newest
            proximo.anterior = newest
        else:  # Bota no final da lista
            newest = Node(valor, anterior=self.cauda)
            self.cauda.proximo = newest
        
    def Dequeue(self, valor):  ## Complexidade O(n)
        '''Remove a primeira ocorrência de um valor na lista.'''
        atual = self.cabeca
        while atual is not None:
            if atual.valor == valor:  # Encontra o nó a ser removido
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo  # Ajusta ponteiro anterior
                else:  # Removendo a cabeça
                    self.cabeca = atual.proximo
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior  # Ajusta ponteiro próximo
                else:  # Removendo a cauda
                    self.cauda = atual.anterior
                self.tamanho -= 1  # Decrementa tamanho da lista
                return
            atual = atual.proximo  # Percorre até encontrar o valor
        raise ValueError('Valor não encontrado na lista.')  # Caso valor não seja encontrado

    def imprimir(self):  ## Complexidade O(n)
        '''Imprime os elementos da lista na ordem.'''
        atual = self.cabeca
        while atual is not None:
            if atual.proximo:
                print(f"{atual.valor} <-> ", end="")  # Formata elementos da lista
            else:
                print(atual.valor, end="")
            atual = atual.proximo  # Percorre até o fim da lista
        print()

if __name__ == "__main__":
    # Criando uma nova lista
    lista = ListaDuplamenteEncadeada()
    
    # Verificar se está vazia no início
    print("Lista está vazia:", lista.esta_vazia())  # Deve retornar True
    print()

    # Adicionar elementos
    print("Inserindo elementos na lista...")
    lista.insert_between(10,)  # Inserindo o primeiro elemento
    lista.insert_between(20, 10)  # Adicionando após o último elemento
    lista.insert_between(30, 20, 10)  # Adicionando após o último elemento
    lista.imprimir()  # Imprime a lista atual
    print()

    # Testando a remoção de elementos
    print("Removendo elemento da lista...")
    lista.Dequeue(20)  # Remove o elemento 20 da lista
    lista.imprimir()  # Imprime a lista atual após remoção
    print()

    # Testando remoção de um elemento inexistente
    print("Tentando remover valor inexistente...")
    try:
        lista.Dequeue(100)  # Tentativa de remover um elemento que não existe
    except ValueError as e:
        print(e)
    print()

    # Testando estado final da lista
    print("Lista final:")
    lista.imprimir()