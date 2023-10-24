import heapq
class Stack :
  def __init__(self):
    self.list=[]

  def push(self,node):
    self.list.append(node)

  def pop(self):
    node = self.list.pop()
    return node
  
  def isEmpty(self):
    if len(self.list) == 0:
      return True
    else :
      return False


class Queue :
  def __init__(self):
    self.list=[]

  def enqueue(self,node):
    self.list.append(node)

  def dequeue(self):
    node = self.list.pop(0)
    return node
  
  def isEmpty(self):
    if len(self.list) == 0:
      return True
    else :
      return False

class PriorityQueue :
  def __init__(self):
    self.list=[]

  def enqueue(self,node):
    self.list.append(node)
    self.list.sort()

  def dequeue(self):
    return self.list.pop(0)
    
  def isEmpty(self):
    if len(self.list) == 0:
      return True
    else :
      return False
  
  def update(self,currentNode,Node):
      for n in self.list:
        if n[1] == Node[0]:
          nw = n[1] + currentNode[0]
          if nw < n[0] :
            n[0]=nw
#Ham ho tro
class PriorityQueue_1:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]