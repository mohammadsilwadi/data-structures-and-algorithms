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
'''test for code challenge 36 '''

def test_graph_depth_first():
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Monstroplolis')
  v4 = graph.add_node('Metroville')
  v5 = graph.add_node('Narnia')
  v6 = graph.add_node('Naboo')
  graph.add_edge(v1, v2)
  graph.add_edge(v1, v4)
  graph.add_edge(v2,v1)
  graph.add_edge(v2,v3)
  graph.add_edge(v2,v4)
  graph.add_edge(v3,v2)
  graph.add_edge(v4,v1)
  graph.add_edge(v4,v2)
  graph.add_edge(v4,v5)
  graph.add_edge(v4,v6)
  graph.add_edge(v6,v4)
  graph.add_edge(v5,v4)
  assert graph.breadth_first_search(v1) == ["Pandora", "Arendelle", "Metroville", "Monstroplolis", "Narnia", "Naboo"]

'''test for code challenge 37 '''

def test_business_trip():
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Monstroplolis')
  v4 = graph.add_node('Metroville')
  v5 = graph.add_node('Narnia')
  v6 = graph.add_node('Naboo')
  graph.add_edge(v1,v2,150)
  graph.add_edge(v1,v3,82)
  graph.add_edge(v2,v3,99)
  graph.add_edge(v2,v4,42)
  graph.add_edge(v3,v4,105)
  graph.add_edge(v3,v5,37)
  graph.add_edge(v3,v6,26)
  graph.add_edge(v4,v6,73)
  graph.add_edge(v5,v6,250)
  city = [v1,v3]
  assert graph.business_trip(city) == (True, '$82')

def test_business_trip_2():
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Monstroplolis')
  v4 = graph.add_node('Metroville')
  v5 = graph.add_node('Narnia')
  v6 = graph.add_node('Naboo')
  graph.add_edge(v1,v2,150)
  graph.add_edge(v1,v3,82)
  graph.add_edge(v2,v3,99)
  graph.add_edge(v2,v4,42)
  graph.add_edge(v3,v4,105)
  graph.add_edge(v3,v5,37)
  graph.add_edge(v3,v6,26)
  graph.add_edge(v4,v6,73)
  graph.add_edge(v5,v6,250)
  city = [v2,v4,v6]
  assert graph.business_trip(city) == (True, '$115')
def test_business_trip_flase():
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Monstroplolis')
  v4 = graph.add_node('Metroville')
  v5 = graph.add_node('Narnia')
  v6 = graph.add_node('Naboo')
  graph.add_edge(v1,v2,150)
  graph.add_edge(v1,v3,82)
  graph.add_edge(v2,v3,99)
  graph.add_edge(v2,v4,42)
  graph.add_edge(v3,v4,105)
  graph.add_edge(v3,v5,37)
  graph.add_edge(v3,v6,26)
  graph.add_edge(v4,v6,73)
  graph.add_edge(v5,v6,250)
  city = [v6,v1]

  assert graph.business_trip(city) == (False, '$0')

