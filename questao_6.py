## Questão 6

class Empty(Exception):
  ''' Error attempting to access an element from an empty container.'''
  pass
#---------------------------------------------
class StaticCircularQueue:
  '''Classe fila circular estática
     - tamanho é determinado na inicialização
     - caso elemento seja adicionado quando a fila estiver cheia, seu tamanho é dobrado
  '''
  #--------------------- nested _Node Class ------------------
  class _Node:
    ''' Lightweight, nonpublic class for storing a singly linked node'''
    _slots_ = ['_element', '_next']

    def __init__(self, element, next):      
      self._element = element               
      self._next = next                      
  # -------------------Queue Methods-----------------------------------

  def __init__(self, size):
    ''' Create an empty queue'''
    self._tail = None         # represents tail of the queue
    self._size = size         # queue static size
    self._len = 0             # numero de elementos na fila

  def is_empty(self):
    ''' Return True if the queue is empty'''
    return self._len == 0

  def is_full(self):
    ''' Return True if the queue is full'''
    return self._size == self._len

  def enqueue(self, e):
    ''' Add an element to the back of the queue'''
    newest = self._Node(e, None)    # new node will be the new tail node
    if self.is_full():
      self._size *= 2
    if self.is_empty():
      newest._next = newest         # initialize circularly
      self._tail = newest            # the tail is the only node
    else:
      newest._next = self._tail._next # new node points to head
      self._tail._next = newest       # old tail points to new node
    self._tail = newest             #  new nodes becomes the tail
    self._len += 1

  def dequeue(self):
    ''' 
    Remove and return the first element of the queue (FIFO)
    Raise Empty exception if the queue is empty
    '''
    if self.is_empty():
      raise Empty('Queue is empty')
    oldhead = self._tail._next      # element is removed from the head
    if self._len == 1:             # removing the only element
      self._tail = None             # queue becomes empty
    else:
      self._tail._next = oldhead._next # bypass old head
    self._len -= 1
    return oldhead._element         

  def _str_(self):
    '''String representation of the queue'''
    arr = ''
    start = self._tail._next
    for i in range(self._len):
      arr += str(start._element) + ', '
      start = start._next
    return '<' + arr + '<'

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