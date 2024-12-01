## Trabalho da disciplina de Estrutura de dados

## Questão 2

# define um novo tipo de exceção para o TAD pilha
class Vazia(Exception):
  ''' Erro ao tentar acessar um elemento de um contêiner vazio.'''
  pass







# arthur viado

class PilhaArray:
  ''' Implementação de pilha LIFO usando uma lista Python como armazenamento subjacente'''

  def _init_(self):
    ''' cria uma pilha vazia'''
    self._dados = []    # instância de lista não pública

  def _len_(self):
    ''' retorna o número de elementos na pilha'''
    return len(self._dados)

  def esta_vazia(self):
    ''' Retorna True se a pilha estiver vazia'''
    return len(self._dados) == 0

  def empilhar(self, e):
    ''' Adiciona o elemento e ao topo da pilha'''
    self._dados.append(e)  # novo item armazenado no final da lista
  
  def topo(self):
    ''' 
    Retorna o elemento no topo da pilha
    Levanta a exceção Vazia se a pilha estiver vazia
    '''
    if self.esta_vazia():
      raise Vazia('A pilha está vazia')
    return self._dados[-1]  # o último item na lista

  def desempilhar(self):
    ''' 
    Remove e retorna o elemento do topo da pilha 
    Levanta a exceção Vazia se a pilha estiver vazia
    '''
    if self.esta_vazia():
      raise Vazia('A pilha está vazia')
    return self._dados.pop()

  def _str_(self):
    ''' 
    Uma representação em string da pilha
    Uma seta mostra o topo da pilha
    '''
    return ''.join(str(self._dados)) + '>'

## Questão 4


