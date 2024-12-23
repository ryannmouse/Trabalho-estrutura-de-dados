class PilhaDinamica:
    
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):  ## complexidade O(1)
        '''Inicializa uma pilha vazia'''
        self._head = None
        self._size = 0

    def pilha_e_vazia(self):  ## complexidade O(1)
        '''Retorna True se a pilha estiver vazia'''
        return self._size == 0
    
    def push(self, e):  ## complexidade O(1)
        '''Adiciona um elemento ao topo da pilha'''
        newest = self._Node(e, self._head)
        self._head = newest
        self._size += 1

    def pop(self):  ## complexidade O(1)
        '''Remove e retorna o elemento do topo da pilha'''
        if self.pilha_e_vazia():
            raise IndexError("Pilha está vazia!")
        valor = self._head._element
        self._head = self._head._next
        self._size -= 1
        return valor
    
    def top(self):  ## complexidade O(1)
        '''Retorna (mas não remove) o elemento do topo da pilha'''
        if self.pilha_e_vazia():
            raise IndexError("Pilha está vazia!")
        return self._head._element
    
    def imprimir(self):  ## complexidade O(n)
        '''Imprime todos os elementos da pilha'''
        arr = ''
        start = self._head
        for i in range(self._size):
            arr += str(start._element) + ', '
            start = start._next
        print('[', arr, '>')

    def imprimir_reversa(self):  ## complexidade O(n)
        '''Imprime todos os elementos da pilha em ordem reversa'''
        arr = []  # Lista auxiliar para armazenar os elementos
        start = self._head  # Começa do topo da pilha
        for i in range(self._size):
            arr.append(start._element)  # Adiciona cada elemento à lista auxiliar
            start = start._next  # Avança para o próximo nó
        print('[', ''.join(str(arr[::-1])), '>')  # Imprime a lista auxiliar em ordem reversa

    def liberar(self):  ## complexidade O(n)
        '''Remove todos os elementos da pilha'''
        for _ in range(self._size):
            self.pop()

    def palindromo(self):  ## complexidade O(n)
        '''Verifica se a pilha é um palíndromo'''
        arr = []  # Lista auxiliar para armazenar os elementos
        start = self._head  # Começa do topo da pilha
        for i in range(self._size):
            arr.append(start._element)  # Adiciona cada elemento à lista auxiliar
            start = start._next  # Avança para o próximo nó
        if arr == arr[::-1]:  # Verifica se a lista é igual à sua reversa
            return True  # Retorna True se for um palíndromo
        else:
            return False  # Retorna False caso contrário
        
    def elimina(self, elemento):  ## complexidade O(n)
        '''Remove a primeira ocorrência de um elemento na pilha'''
        elementos_de_cima = PilhaDinamica()  # Pilha auxiliar para armazenar elementos temporariamente
        achou = False  # Flag para indicar se o elemento foi encontrado
        for _ in range(self._size):
            elemento_atual = self.pop()  # Remove o elemento do topo da pilha
            elementos_de_cima.push(elemento_atual)  # Adiciona o elemento na pilha auxiliar
            if elemento_atual == elemento:
                achou = True  # Marca que o elemento foi encontrado
                break
        if not achou:
            raise ValueError('Elemento não encontrado')  # Levanta exceção se o elemento não for encontrado
        # Reinsere os elementos da pilha auxiliar de volta na pilha original, exceto o elemento removido
        for elemento in elementos_de_cima.imprimir().strip('<')[1:]:
            self.push(elemento)

    def pares_e_impares(self, lista):  ## complexidade O(n)
        '''Separa os elementos da lista em duas pilhas: uma de pares e outra de ímpares'''
        pares = PilhaDinamica()  # Pilha para armazenar números pares
        impares = PilhaDinamica()  # Pilha para armazenar números ímpares
        for i in lista:
            if i % 2 == 0:
                pares.push(i)  # Adiciona número par na pilha de pares
            else:
                impares.push(i)  # Adiciona número ímpar na pilha de ímpares
        return pares, impares  # Retorna as duas pilhas