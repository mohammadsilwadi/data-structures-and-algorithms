import pytest
from stack_and_queue.stack_queue_pseudo import Pseudo_queue

def test_cases_pseudo():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
