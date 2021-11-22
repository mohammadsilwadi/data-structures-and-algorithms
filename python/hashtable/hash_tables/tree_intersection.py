from hash_tables.hash_table import HashTable

class Node:
    def __init__(self,data):
       self.right=None
       self.left=None
       self.data=data
       self.next=None

class BinaryTree:

  def __init__(self):
        self.root = None
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
  def tree_intersection(self ,tree1, tree2 ,hashtable):

        hashtable = HashTable()
        listtree1 = tree1.pre_order()
        for item in listtree1:
            hashtable.add(str(item),item)
        arr=[]
        listtree2 = tree2.pre_order()
        for element in listtree2:
            if hashtable.contains(str(element)):
                arr.append(element)
            else:
                hashtable.add(str(element), element)

        return arr


if __name__ == "__main__":
    tree1= BinaryTree()
    tree1.root = Node(150)
    tree1.root.left = Node(100)
    tree1.root.right = Node(250)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(500)


    tree2= BinaryTree()
    tree2.root = Node(42)
    tree2.root.left = Node(100)
    tree2.root.right = Node(600)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.left = Node(4)
    tree2.root.right.right.right = Node(500)

    hashtable = HashTable()
    tree = BinaryTree()
    intersectionList = tree.tree_intersection(tree1, tree2 , hashtable)
    print(intersectionList)
