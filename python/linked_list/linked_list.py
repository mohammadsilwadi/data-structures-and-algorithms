class Node:
    """
    A class representing a Node
    """
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

class LinkedList:
    """
      A class for creating instances of a Linked List.
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """"
        Adds a new node with that value to the head of the list with an O(1) Time performance.
        """
        # create new node
        node = Node(value)
        if not self.head:
              self.head = node
        else:
              data = self.head
              self.head = node
              self.head.next = data

    def includes(self, data):
        """Indicates whether that value exists as a Node’s value somewhere within the list.
        """
        value=self.head
        while value :
          if value.data==data:
              value= value.next
              return True
          else:
              return False
    def str(self):
        """ Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL" """
        current=self.head
        value = ""
        while current:
            value+= f"{str(current.value)}=>"
            current = current.next
        value += "NULL"
        return value
