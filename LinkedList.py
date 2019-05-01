class Node(object):
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList(object):
  def __init__(self, head=None):
    self.head = head
    self.__size__ = 0

  def isEmpty(self):
    if self.head:
      return False
    
    return True

  def size(self):
    return self.__size__

  def append(self, node):
    if self.isEmpty():
      self.head = node
    else:
      current = self.head
      while current.next:
        current = current.next
        
      current.next = node
    
    self.__size__ += 1

  def insert(self, node, index):
    n = Node(node.value, node.next)

    if self.isEmpty():
      self.head = n
    elif index < 0:
      n.next = self.head
      self.head = n
    elif index > self.size():
      self.append(n)
      self.__size__ -= 1
    else:
      current = self.head

      for _ in range(index - 1):
        current = current.next
      n.next = current.next
      current.next = n

    self.__size__ += 1

  def remove(self, value):
    if self.isEmpty():
      return None
    elif self.head.value == value:
      removed = self.head
      self.head = self.head.next
      removed.next = None
      self.__size__ -= 1

      return removed
    else:
      previous = self.head
      current = previous.next
      while current:
        if current.value == value:
          removed = current
          previous.next = current.next
          removed.next = None
          self.__size__ -= 1

          return removed
        previous = current
        current = current.next

    return None

  def printList(self):
    if self.isEmpty():
      print('List is empty')

    current = self.head
    while current:
      print(current.value)
      current = current.next