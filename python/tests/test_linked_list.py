from linked_list.linked_list import LinkedList,Node
import pytest
# 1-Can successfully instantiate an empty linked list
def test_node_has_int_data():
  expected = None
  ll = LinkedList()
  actual = ll.head
  assert actual == expected
## 2-Can properly insert into the linked list
def test_node_has_str_data():
    expected = "a"
    node = Node("a")
    actual = node.data
    assert actual == expected
# 3-The head property will properly point to the first node in the linked list
def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()
  ll.insert(1)
  node = ll.head
  actual = node.data
  assert actual == expected
#4-Can properly insert multiple nodes into the linked list
def test_linked_list_insert_twice():
  # Arrange
  expected = 0
  ll = LinkedList()
  # Act
  ll.insert(1)
  ll.insert(0)
  node = ll.head
  actual = node.data
  # Assert
  assert actual == expected
  assert ll.head.next.data == 1
#5-Will return true when finding a value within the linked list that exists
def test_includes_True():
    expected = True
    ll=LinkedList()
    ll.insert(1)
    actual = ll.includes(1)
    expected = True
    assert actual == expected
#6-Will return false when searching for a value in the linked list that does not exist
def test_includes_False():
    expected = False
    ll=LinkedList()
    ll.insert(0)
    actual = ll.includes(1)
    expected = False
    assert actual == expected
#7-Can properly return a collection of all the values that exist in the linked list
def test_return_all_values():
    ll = LinkedList()
    ll.append('m')
    ll.append('o')
    ll.append('h')
    actual = ll.__str__()
    expected = '( m ) -> ( o ) -> ( h ) -> None'
    assert actual == expected
# 8- test the append value function in the linked list
def test_append_value():
  expected = 9
  ll = LinkedList()
  ll.append(9)
  node = ll.head
  actual = node.data
  assert actual == expected
#9- Can successfully add multiple nodes to the end of a linked list
def test_multi_to_the_end():
    ll = LinkedList()
    ll.append(5)
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(2)
    actual = ll.__str__()
    expected = '( 5 ) -> ( 4 ) -> ( 3 ) -> ( 2 ) -> ( 2 ) -> None'
    assert actual == expected

#Can successfully insert a node before a node located i the middle of a linked list

###################################-insert-after-middle-##################################################
def test_after_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 'added')
    actual = ll.__str__()
    expected = '( 1 ) -> ( 2 ) -> ( added ) -> ( 3 ) -> None'
    assert actual == expected

