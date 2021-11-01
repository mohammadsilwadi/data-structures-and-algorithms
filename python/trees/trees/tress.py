
#################################
#####code challenge 15 , 16 and 17####
#################################

# tree implementation
"""
This Module defines a Node and a Binary Tree
"""
from trees.breadth_first import Queue
class Node:
    def __init__(self,data):
       self.right=None
       self.left=None
       self.data=data
       self.next=None





class BinaryTree:

  def __init__(self):
        self.root = None

  def bfs(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    # Queue breadth <-- new Queue()
    breadth = Queue()
    # breadth.enqueue(root)
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items
  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """
    list_of_items = []
    def walk(node):
      if node:
        list_of_items.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def in_order(self):
    """
    A binary tree method which returns a list of items in order

    input: None

    output: tree items

    sub method : walk () to make the recursion
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)

    walk(self.root)
    return list_of_items
  def tree_max(self):
        """find max value in tree"""
        if self.root is None:
            return None
        max = self.root.data
        def find_max(root):
            nonlocal max
            if root.data > max:
                max = root.data
            if root.left is not None:
                find_max(root.left)
            if root.right is not None:
                find_max(root.right)
        find_max(self.root)
        return max


class Binary_search_tree(BinaryTree):
    """
    Binary class to add a values in tree and search about specific value
    """
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while current:
            if value > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
    def contains(self, value):
        """Returns True if value is in the BST, False otherwise"""
        current = self.root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False


if __name__ == '__main__':
    tree = BinaryTree()

