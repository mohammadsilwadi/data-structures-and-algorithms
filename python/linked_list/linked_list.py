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
        self.head = Node(value, self.head)


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

        """ Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL" """
    def __str__(self):
        output = ""
        current = self.head
        while current:
            value = current.data
            if current.next is None:
                output += f"( {value} ) -> None"
                break
            output = output + f"( {value} ) -> "
            current = current.next
        return output
    def append(self, value='null'):

          node = Node(value)
          if not self.head:
              self.head = node

          else:
              crrval = self.head
              while crrval.next != None:
                  crrval = crrval.next
              crrval.next = node
    """
    Code Challenge: Class 06
    """
    """
    insert before adds a new node with the given new value
    immediately before the first node that has the value specified
    """
    def insert_before(self, value, new):
        current = self.head
        if current.data == value:
            self.insert(new)
        else:
          while current:
             if current.next.data == value:
                value = current.next
                current.next = Node(new)
                current.next.next = value
                break
             current = current.next
    """
    insert after adds a new node with the given new value
    immediately after the first node that has the value specified

    """
    def insert_after(self, value, new):
        current = self.head
        while current:
            if current.data == value:
                value = current.next
                current.next = Node(new)
                current.next.next = value
                break
            current = current.next
