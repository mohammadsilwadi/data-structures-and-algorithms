from trees.tree_fizz_buzz import *

def test_If_the_value_is_divisible_by_3():
    tree= KTree()
    tree.root = Node(3)
    excepted = 'Fizz'
    actual = fizz_buzz_tree(tree.root).value
    assert excepted == actual

def test_If_the_value_is_divisible_by_5():
    tree= KTree()
    tree.root = Node(3)
    tree.root.children.append(Node(5))
    excepted = 'Buzz'
    actual = fizz_buzz_tree(tree.root).children[0].value
    assert excepted == actual

def test_If_the_value_is_divisible_by_3_and_5_():
    tree= KTree()
    tree.root = Node(3)
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(15))
    excepted = 'FizzBuzz'
    actual = fizz_buzz_tree(tree.root).children[1].value
    assert excepted == actual

def test_If_the_value_is_not_divisible_by_3_or_5():
    tree= KTree()
    tree.root = Node(3)
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(2))
    excepted = '2'
    actual = fizz_buzz_tree(tree.root).children[1].value
    assert excepted == actual
