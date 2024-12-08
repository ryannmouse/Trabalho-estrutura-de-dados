## Trabalho da disciplina de Estrutura de dados

## Questão 2

# define um novo tipo de exceção para o TAD pilha
class Vazia(Exception):
  '''Erro ao tentar acessar um elemento de um contêiner vazio.'''
  pass

class PilhaArray:
  '''Implementação de pilha LIFO usando uma lista Python como armazenamento subjacente'''

  def __init__(self):
    '''Cria uma pilha vazia'''
    self._dados = []    # instância de lista não pública

  def _len_(self): ## Complexidade O(1)
    '''Retorna o número de elementos na pilha'''
    return len(self._dados)

  def esta_vazia(self): ## Complexidade O(1)
    '''Retorna True se a pilha estiver vazia'''
    return len(self._dados) == 0

  def push(self, e): ## Complexidade O(1)
    '''Adiciona o elemento e ao topo da pilha'''
    self._dados.append(e)  # novo item armazenado no final da lista
  
  def top(self): ## Complexidade O(1)
    '''Retorna o elemento no topo da pilha'''
    if self.esta_vazia():
      raise Vazia('A pilha está vazia')
    return self._dados[-1]  # o último item na lista

  def pop(self): ## Complexidade O(1)
    '''Remove e retorna o elemento do topo da pilha'''
    if self.esta_vazia():
      raise Vazia('A pilha está vazia')
    return self._dados.pop()

  def _str_(self): ## Complexidade O(n)
    '''Uma representação em string da pilha'''
    return ''.join(str(self._dados)) + '>'
  
  def imprimir(self): ## Complexidade O(n)
   '''Imprime a pilha'''
   print(self._str_())
 
  def imprimir_reversa(self): ## Complexidade O(n)
    '''Imprime a pilha de forma reversa'''
    reverso = '<' + ''.join(str(self._dados[::-1]))
    print(reverso)

  def liberar(self): ## Complexidade O(n)
    '''Remove todos os elementos da pilha'''
    for _ in range(len(self._dados)):
      self._dados.pop()

  def palindromo(self): ## Complexidade O(n)
    '''Verifica se a pilha é um palíndromo'''
    if self._dados == self._dados[::-1]:
      return True
    else:
      return False
    
  def elimina(self, elemento): ## Complexidade O(n)
    '''Remove um elemento da pilha'''
    elementos_de_cima = []
    achou = False
    for _ in range(len(self._dados)):
      elemento_atual = self._dados.pop()
      elementos_de_cima.append(elemento_atual)
      if elemento_atual == elemento:
        achou = True
        break

    if not achou:
      raise ValueError('Elemento não encontrado')

    for elemento in elementos_de_cima[1:]:
      self.push(elemento)

  def pares_e_impares(self): ## Complexidade O(n)
    '''Separa os números pares e ímpares em duas pilhas diferentes'''
    # pedir os números para o usuário
    pilha = PilhaArray()

    while True:
      try:
        num = int(input('Digite um número inteiro positivo (0 para parar): '))
        if num <= 0:
          break
        pilha.push(num)
      except ValueError:
        print('Digite um número inteiro válido!')

    pares = PilhaArray()
    impares = PilhaArray()
    for num in pilha._dados:
      if num % 2 == 0:
        pares.push(num)
      else:
        impares.push(num)
    return pares, impares
  

  
