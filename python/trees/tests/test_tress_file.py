
from trees.tress import BinaryTree, Node
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
