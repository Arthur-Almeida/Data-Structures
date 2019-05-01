class Node(object):
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class Stack(object):
  def __init__(self, top=None):
    self.top = top
    self.__size__ = 0

  def isEmpty(self):
    return self.top == None

  def size(self):
    return self.__size__

  def push(self, node):
    n = Node(node.value)
    if self.isEmpty():
      self.top = n
    else:
      n.next = self.top
      self.top = n
    self.__size__ += 1

  def pop(self):
    removed = self.top
    self.top = self.top.next
    removed.next = None
    self.__size__ -= 1

    return removed

  def peek(self):
    return self.top

  def printStack(self):
    if self.isEmpty():
      print('Stack is empty')
    
    current = self.top
    while current:
      print(current.value)
      current = current.next


