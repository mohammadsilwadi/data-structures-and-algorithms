
from trees.tress import BinaryTree, Node
# def test_bfs():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for A,B,C,D
#   a_node = Node('A')
#   b_node = Node('B')
#   c_node = Node('C')
#   d_node = Node('D')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node

#   # set expected list
#   expected = ["A", "B", "C", "D"]
#   # set actual to return value of bfs call
#   actual = tree.bfs()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_bfs passed")

# def test_bfs_2():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for A,B,C,D
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node

#   # set expected list
#   expected = ["1", "2", "3", "4"]
#   # set actual to return value of bfs call
#   actual = tree.bfs()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_bfs_2 passed")

# def test_pre_order():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for 1,2,3,4
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node

#   # set expected list
#   expected = ["1", "2", "4", "3"]
#   # set actual to return value of pre_order call
#   actual = tree.pre_order()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_pre_order_ passed")

# def test_post_order():
#   # Arrange
#   # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for 1,2,3,4
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node

#   # set expected list
#   expected = ["4", "2", "3", "1"]
#   # set actual to return value of post_order call
#   actual = tree.post_order()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_post_order_ passed")

# def test_in_order():
  # Arrange
  # Create tree instance
#   tree = BinaryTree()

#   # Create Nodes for 1,2,3,4
#   a_node = Node('1')
#   b_node = Node('2')
#   c_node = Node('3')
#   d_node = Node('4')
#   a_node.left = b_node
#   a_node.right = c_node
#   b_node.left = d_node

#   # Add Root node to tree
#   tree.root=a_node

#   # set expected list
#   expected = ["4", "2", "1", "3"]
#   # set actual to return value of in_order call
#   actual = tree.in_order()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_in_order_ passed")
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
