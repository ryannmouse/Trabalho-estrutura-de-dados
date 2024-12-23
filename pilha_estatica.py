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
    
