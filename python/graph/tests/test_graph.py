from graph import __version__


import pytest

from graph.graph import  Graph, Vertex
""" Node can be successfully added to the graph"""
def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected


'''An empty graph properly returns zero'''
def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected

'''The proper size is returned, representing the number of nodes in the graph'''
def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected

'''An edge can be successfully added to the graph'''
def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

"""A collection of all nodes can be properly retrieved from the graph"""
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected

"""All appropriate neighbors can be retrieved from the graph"""
'''Neighbors are returned with the weight between nodes included'''
def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44
