from stack_and_queue.stack_and_queue import Stack, Queue,Node
import pytest
# Stack tests
# test 1 Can successfully push onto a stack
def test_push():
    stack = Stack()
    stack.push(1)
    actual = stack.top.value
    expected = 1
    assert actual == expected
# test 2 Can successfully push multiple values onto a stack
def test_push_multiple_values(stack):
    actual = stack.top.value
    expected = "cat"
    assert actual == expected
# test 3 Can Can successfully pop off the stack
def test_pop():
    stack = Stack()
    stack.push(1)
    actual = stack.pop()
    expected = 1
    assert actual == expected
# test 4 Can successfully empty a stack after multiple pops
def test_pop_multiple():
    stack = Stack()
    stack.push(1)
    actual = stack.pop()
    stack.push(2)
    actual = stack.pop()
    expected = 2
    assert actual == expected
    assert stack.is_empty() == True
# 5-Can successfully instantiate an empty stack
def test_is_empty_stack():
    stack=Stack()
    assert stack.is_empty() == True
# 6-Can successfully peek the next item on the stack
def test_peek(stack):
    actual=stack.peek()
    expected='cat'
    assert actual == expected
# 7-Calling pop or peek on empty stack raises exception
def test_exception():
    with pytest.raises(Exception):
     stack = Stack()
     stack.peek()
     stack.pop()
# decorator
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("cat")
    return stack
#"Queue tests"
# 8-Can successfully enqueue into a queue
def test_enqueue():
    queue=Queue()
    queue.enqueue(1)
    actual=queue.rear.value
    expected=1
    assert actual == expected
# 9-Can successfully enqueue multiple values into a queue
def test_enqueue_multiple(queue):
    actual=queue.rear.value
    expected="Python"
    assert actual == expected
# 10-Can successfully dequeue out of a queue the expected value
def test_dequeue_multiple(queue):
    actual = queue.dequeue()
    expected=1
    assert actual == expected
# 11-Can successfully peek into a queue, seeing the expected value
def test_dequeue_peek(queue):
    actual = queue.peek()
    expected=1
    assert actual == expected
# 12-Can successfully empty a queue after multiple dequeues
def test_empty(queue):
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == "Python"
    assert queue.is_empty() == True
# 13-Can successfully instantiate an empty queue
def test_is_empty_queue():
    queue=Queue()
    assert queue.is_empty() == True
    # assert queue.is_empty()
# 14-Calling dequeue or peek on empty queue raises exception
def test_exception_2():
    with pytest.raises(Exception):
     queue = Queue()
     queue.dequeue()
     queue.peek()

@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("Python")
    return queue
