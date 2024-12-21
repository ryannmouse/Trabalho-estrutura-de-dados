## Questão 6

class Empty(Exception):
  ''' Erro ao tentar acessar um elemento de um contêiner vazio.'''
  pass
#---------------------------------------------
class StaticCircularQueue:
  '''Classe fila circular estática
     - tamanho é determinado na inicialização
     - caso elemento seja adicionado quando a fila estiver cheia, seu tamanho é dobrado
  '''
  #--------------------- nested _Node Class ------------------
  class _Node:
    ''' Classe leve e não pública para armazenar um nó encadeado individual'''
    _slots_ = ['_element', '_next']

    def __init__(self, element, next):      
      self._element = element               
      self._next = next                      
  # -------------------Métodos da Fila------------------------

  def __init__(self, size):
    ''' Cria uma fila vazia'''
    self._tail = None         # representa a cauda da fila
    self._size = size         # tamanho estático da fila
    self._len = 0             # número de elementos na fila

  def is_empty(self):  # Complexidade O(1)
    ''' Retorna True se a fila estiver vazia'''
    return self._len == 0

  def is_full(self):  # Complexidade O(1)
    ''' Retorna True se a fila estiver cheia'''
    return self._size == self._len

  def enqueue(self, e):  # Complexidade O(1)
    ''' Adiciona um elemento ao final da fila'''
    newest = self._Node(e, None)        # novo nó será o novo nó da cauda
    if self.is_full():
      self._size *= 2
    if self.is_empty():
      newest._next = newest             # inicializa circularmente
      self._tail = newest               # a cauda é o único nó
    else:
      newest._next = self._tail._next   # novo nó aponta para a cabeça
      self._tail._next = newest         # antiga cauda aponta para o novo nó
    self._tail = newest                 # novo nó se torna a cauda
    self._len += 1

  def dequeue(self):  # Complexidade O(1)
    ''' 
    Remove e retorna o primeiro elemento da fila (FIFO)
    Levanta uma exceção Empty se a fila estiver vazia
    '''
    if self.is_empty():
      raise Empty('Queue is empty')
    oldhead = self._tail._next      # elemento é removido da cabeça
    if self._len == 1:              # removendo o único elemento
      self._tail = None             # fila se torna vazia
    else:
      self._tail._next = oldhead._next  # ignora a antiga cabeça
    self._len -= 1
    return oldhead._element         

  def _str_(self):  # Complexidade O(n)
    '''Representação em string da fila'''
    arr = ''
    start = self._tail._next               # começa na cabeça da fila
    for i in range(self._len):             
      arr += str(start._element) + ', '    # adiciona elementos à string
      start = start._next                  # avança para o próximo nó
    return '<' + arr + '<'                 # retorna a string formatada

######################

if __name__ == '__main__':

  Q = StaticCircularQueue(4)
  Q.enqueue(5)
  Q.enqueue(3)
  Q.enqueue(2)

  print(Q._str_())

  Q.dequeue()
  Q.dequeue()
  Q.dequeue()
  Q.dequeue()

  print(Q._str_())