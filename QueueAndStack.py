import queue as q

class myStack():

  def __init__(self):
    self.lista = []

  # Métodos de entrada: push/put
  def push(self, dato):
    self.lista.append(dato)

  # Métodos de salida: pop/get
  def pop(self):
    dato = self.lista[-1]
    self.lista = self.lista[:-1]
    return dato

  def empty(self):
    return len(self.lista) == 0

  def top(self):
    dato = self.lista[0]
    return dato

class myQueue():

  def __init__(self):
    self.lista = []

  # Métodos de entrada: push/put
  def push(self, dato):
    self.lista.append(dato)

  # Métodos de salida: pop/get
  def pop(self):
    dato = self.lista[0]
    self.lista = self.lista[1:]
    return dato

  def empty(self):
    return len(self.lista) == 0

  def top(self):
    dato = self.lista[0]
    return dato

# PERSONAS

lista = ["Carlos", "Maryelin", "Jefferson", "Wendrys", "Dalvin", "Susana"]

# QUEUE

print("QUEUE:")

newQueue = q.Queue()
for name in lista:
  newQueue.put(name)

pipeline = ""
while not newQueue.empty():
  pipeline += str(newQueue.get()) + " "
print(pipeline)

# STACK

print("STACK:")

newStack = q.LifoQueue()
for name in lista:
  newStack.put(name)

pipeline = ""
while not newStack.empty():
  pipeline += str(newStack.get()) + " "
print(pipeline)

# PRIORITY QUEUE

print("PRIORITY QUEUE:")

lista_priorizada = [(4, "Carlos"), (2, "Maryelin"), (1, "Jefferson"), (3, "Wendrys"), (4, "Dalvin"), (8, "Susana")]

newPriorityQueue = q.PriorityQueue()
for name in lista_priorizada:
  newPriorityQueue.put(name)

pipeline = ""
while not newPriorityQueue.empty():
  pipeline += str(newPriorityQueue.get()[1]) + " "
print(pipeline)