class Node:
    def __init__(self,data):
       self.right=None
       self.left=None
       self.data=data
       self.next=None


class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

