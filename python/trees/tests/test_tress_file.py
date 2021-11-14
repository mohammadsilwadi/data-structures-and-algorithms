from trees.tress import BinaryTree, Node
from trees.breadth_first import *
'''ch 15'''
""" Can successfully instantiate an empty tree"""
def test_empty_tree():
    tree = BinaryTree()
    assert tree.root is None
'''Can successfully instantiate a tree with a single root node'''
def test_root_node():
    tree = BinaryTree()
    a_node = Node('1')
    tree.root = a_node
    expected='1'
    actual = tree.root.data
    assert expected == actual
'''Can successfully add a left child and right child to a single root node'''
def test_add_lr_node():
    tree = BinaryTree()
    a_node = Node('1')
    b_node= Node('2')
    c_node= Node('3')
    tree.root= a_node
    a_node.left= b_node
    a_node.right=c_node
    expected='2'
    actual=tree.root.left.data
    assert expected == actual
    expected='3'
    actual=tree.root.right.data
    assert expected == actual
'''Can successfully return a collection from a preorder traversal'''
def test_pre_order():
  tree = BinaryTree()
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node
  tree.root=a_node
  expected = ["1", "2", "4", "3"]
  actual = tree.pre_order()
  assert actual == expected
""""Can successfully return a collection from an inorder traversa"""
def test_in_order():
  tree = BinaryTree()
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node
  tree.root=a_node
  expected = ["4", "2", "1", "3"]

  actual = tree.in_order()

  assert actual == expected

  '''Can successfully return a collection from a postorder traversal'''
def test_post_order():
  tree = BinaryTree()
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node
  tree.root=a_node

  expected = ["4", "2", "3", "1"]

  actual = tree.post_order()

  assert actual == expected
  print("test_post_order_ passed")
  """ ch 16"""
'''Can successfully get max value  '''
def test_get_max():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(15)
    tree.root.right = Node(30)
    tree.root.left.left = Node(8)
    expected = 30
    actual = tree.tree_max()
    assert actual == expected
''' return None if the tree is empty'''
def test_max_value_empty_tree():
    tree = BinaryTree()
    assert tree.tree_max() == None
""" ch 17"""
'''Can successfully return a collection from a breadth first '''
def test_bfs():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('A')
  b_node = Node('B')
  c_node = Node('C')
  d_node = Node('D')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["A", "B", "C", "D"]
  # set actual to return value of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs passed")

