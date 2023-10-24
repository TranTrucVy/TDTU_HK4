class Stack():
    def __init__(self):
        self.items = []

    def __str__(self) -> str:
        return str(self.items)
    
    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def contain(self, item):
        return item in self.items
    
    def peek(self):
        return self.items[-1]

class Queue():
    def __init__(self):
        self.items = []
    
    def __str__(self) -> str:
        return str(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def contain(self, item):
        return item in self.items
    
    def empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]

class PriorityQueue():
    def __init__(self):
        self.items = []
    
    def __str__(self) -> str:
        return str(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
        self.items.sort(key = lambda i: i[0])
    
    def dequeue(self):
        return self.items.pop(0)
    
    def contain(self, item):
        return item in [it[1] for it in self.items]

    def getPriority(self, k):
        for w, v in self.items:
            if v == k:
                return w
        raise 'KeyError'
    
    def empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]