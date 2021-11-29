from collections import deque


class Vertex:
    """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """
    def __init__(self, value):
        """
    Initalization for a Vertex to hold a value.

    """
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
         self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        """
		The constructor method for the stack class and it initializes
        the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
		Store the passed value in a node and then push the node on top of the stack.

		PARAMETERS
		----------
			value: any
			The value that will get stored in a node to be pushed on top of the stack.
		"""
        self.dq.append(value)

    def pop(self):
        """
		Return the top node in a stack.
		"""
        self.dq.pop()


class Edge:
    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

  """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
        Initalization for a hashmap to hold the vertices
        """
        self._adjacency_list = {}

    def add_node(self, value):
        """
        Method for Adding a node to the graph
        Arguments: value
        Returns: The added node
        """
        # new node
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Method to get all nodes in Graph
        Arguments: None
        return: All nodes
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ """
        return self._adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex):
        queue = Queue()
        visited = set()
        nodes = []
        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            nodes.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return nodes

    def business_trip(self,cities):
        if len(cities) == 0:
            return False,'$0'
        if self._adjacency_list[cities[0]] == []:
            return False,'$0'
        sum = 0
        flag = False
        for i in range(len(cities)-1):
            neighbors = self._adjacency_list[cities[i]]
            for neighbor in neighbors:
                if cities[i+1].value == neighbor.vertex.value:
                    sum += neighbor.weight
                    flag = True
                    break
                else:
                    sum += 0
                    flag = False
        if not flag:
            return False,'$0'
        return True,'$'+ str(sum)

if __name__ == '__main__':
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Metroville')
  v4 = graph.add_node('Monstroplolis')
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
#   print(graph.print_djacency_list())
  cities = [v1,v3]
  print(graph.business_trip(cities))
  cities2 = [v2,v4,v6]
  print(graph.business_trip(cities2))
  cities3 = [v6,v1]
  print(graph.business_trip(cities3))
  cities4 = [v6]
  print(graph.business_trip(cities4))
  cities5 = [v1,v2,v3,v4,v5,v6]
  print(graph.business_trip(cities5))
