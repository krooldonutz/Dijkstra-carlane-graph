__author__ = "Sayyidina Shaquille Malcolm 32578393"
class MinHeap():
    def __init__(self) -> None:
        """
        MinHeap concept inspired by PASS tutor Jia Khor

        This is a constructor function that initializes two instance variables, an array and a length, to
        None and 0 respectively.
        Time complexity: O(1)
        Aux Space complexity: O(V), V's the number of elements in the MinHeap
        """
        self.array = [None]
        self.length = 0

    def insert(self, element: tuple[int,any]):
        """
        This function inserts a tuple element into an array and increases the length of the array while
        calling another function called "rise". This MinHeap is versatile and can be used by any elements of any kind as long
        the first index of the tuple has the integer it's trying to prioritize with
        
        :param element: The "element" parameter is a tuple that contains two values: an integer and any
        other data type. This method is used to insert this tuple into an array
        :type element: tuple[int,any]

        Time Complexity: O(log V), V is the number of elements in the MinHeap (caused by calling the rise method)
        Aux Space Complexity: O(1)
        """
        self.array.append(element)
        self.length += 1
        self.rise(self.length)
    
    def serve(self):
        """
        This function serves as a method to remove and return the highest priority element from a heap
        data structure.

        :return: the element that was removed from the heap, which is the root node of the heap after it
        has been swapped with the last element and sunk down to its correct position.

        Time Complexity: O(log V), V is the number of elements in the MinHeap (caused by calling the sink method)
        Aux Space Complexity: O(1)

        """
        self.swap(1, self.length)
        self.length -= 1
        self.sink(1)
        return self.array.pop()
    
    def swap(self, x, y):
        """
        The function swaps the values of two elements in an array.
        
        :param x: The index of the first element to be swapped in the array
        :param y: The parameter `y` is a variable that represents the index of an element in an array
        that we want to swap with another element

        Time Complexity: O(1)
        Aux Space Complexity: O(1)
        """
        self.array[x], self.array[y] = self.array[y], self.array[x]
    
    def rise(self, element_int: int):
        """
        This function implements the "rise" operation in a binary heap data structure.
        
        :param element_int: The index of the element in the heap that needs to be "risen" (moved up) to
        maintain the heap property
        :type element_int: int

        Time Complexity: O(log V), V is the number of elements in the MinHeap
        Aux Space Complexity: O(1)
        """
        element = self.array[element_int]
        parent_idx = element_int // 2
        while parent_idx >= 1:
            parent = self.array[parent_idx]
            if parent[0] > element[0]:
                self.swap(parent_idx, element_int)
                element_int = parent_idx
                parent_idx = element_int // 2
            else:
                break
    
    def sink(self, element_int: int):
        """
        This is a Python implementation of the "sink" operation for a binary heap data structure.
        
        :param element_int: The parameter `element_int` is an integer representing the index of the
        element in the heap that needs to be sunk down to its correct position
        :type element_int: int

        Time Complexity: O(log V), V is the number of elements in the MinHeap
        Aux Space Complexity: O(1)
        """
        child_idx = 2 * element_int
        while child_idx <= self.length:
            child = self.array[child_idx]
            if child_idx < self.length and self.array[child_idx+1][0] < child[0]:
                child = self.array[child_idx+1]
                child_idx += 1
            if self.array[element_int][0] > child[0]:
                self.swap(element_int, child_idx)
                element_int = child_idx
                child_idx = 2 * element_int
            else:
                break

# This is a Python class for representing a graph data structure, with methods for adding vertices and
# edges, checking for connectivity between vertices, and printing the graph.
class Graph:
    def __init__(self, v: tuple) -> None:
        """
        This function initializes a graph with vertices and edges based on a given list of pairs and
        their weights.
        
        :param v: The parameter `v` is a list of tuples, where each tuple represents an edge in a graph.
        Each tuple contains four elements: the ID of the first vertex, the ID of the second vertex, the
        carpool lane weight of the edge, and the alone lane wight of the edge

        Time complexity = O(n) where n is the length of the tuple
        Aux Space complexity = O(V) where V is the length of the tuple
        """
        max_id = max(max(pair[0],pair[1]) for pair in v)
        self.vertices = [None] * (max_id + 1)
        for i in range(len(v)):
            self.vertices[v[i][0]] = Vertex(v[i][0])
            self.vertices[v[i][1]] = Vertex(v[i][1])
        for i in range(len(v)):
            self.add_edge(self.vertices[v[i][0]], self.vertices[v[i][1]], v[i][2], v[i][3])

    def __len__(self) -> int:
        """
        This function returns the length of the vertices list in the object.
        :return: The length of the list of vertices in the object is being returned as an integer.
        """
        return len(self.vertices)
    
    def __str__(self) -> str:
        """
        This function returns a string representation of a graph object, including information about
        each vertex and its neighbors.
        :return: The `__str__` method is returning a string representation of the graph object. The
        string contains information about each vertex in the graph and its neighbors. The output
        includes the label of each vertex and a list of its neighboring vertices.

        Time complexity: O(n) n is the length of the vertices
        """
        output = ""
        for vertex in self.vertices:
            output += "Vertex " + str(vertex) + "\n" + " Neighbours " + ", ".join(str(edge) for edge in vertex.edges) + "\n"
        return output

    
    def add_edge(self, source: 'Vertex', dest: 'Vertex', weight_alone, weight_carpool):
        """
        This function adds an edge between two vertices with given weights for alone and carpool travel.
        
        :param source: The starting vertex of the edge being added
        :type source: 'Vertex'
        :param dest: The 'dest' parameter is a Vertex object representing the destination vertex of the
        edge being added
        :type dest: 'Vertex'
        :param weight_alone: The weight of the edge when the source vertex travels alone (without
        carpooling)
        :param weight_carpool: `weight_carpool` is a parameter that represents the weight or cost of
        using a carpool to travel from the source vertex to the destination vertex. It is used in graph
        algorithms that involve finding the shortest path or minimum cost path between two vertices in a
        graph
        """
        source.edges.append(Edge(dest, weight_alone, weight_carpool))
    
    def has_way_to(self, start: 'Vertex', end: 'Vertex') -> bool:
        """
        The function checks if there is a path between two vertices by iterating through the edges of
        the starting vertex and checking if the destination vertex matches the end vertex.
        
        :param start: Vertex object representing the starting vertex of the path being checked
        :type start: 'Vertex'
        :param end: The 'end' parameter is a Vertex object representing the destination vertex of an
        edge
        :type end: 'Vertex'
        :return: The function `has_way_to` takes two arguments, `start` and `end`, both of which are
        instances of the `Vertex` class. The function checks if there is a direct edge from `start` to
        `end` by iterating over the edges of `start` and checking if the destination of each edge is
        `end`. If such an edge is found, the function returns `True

        Time complexity: O(n) where n is the number of edges in the source vertex
        Aux Space complexity: O(1)
        """
        for edge in start.edges:
            if edge.dest == end:
                return True
        return False

# The Vertex class represents a vertex in a graph and contains various attributes such as edges,
# visited status, previous vertex, distance, cycle status, and change.
class Vertex:
    def __init__(self, id:int) -> None:
        """
        This is the constructor function for a Vertex class that takes an integer ID as a parameter.
        
        :param id: The `id` parameter is an integer that is passed as an argument to the constructor of
        a class. Where it labels the Vertex.
        :type id: int
        """
        self.id = id
        self.edges = []
        self.visited = False
        self.previous = None
        self.distance = float('inf')
        self.cycle = False
        self.change = 0
    
    def __str__(self) -> str:
        output = str(self.id)
        return output


class Edge:
    """"
    The Edge class represents an edge in a graph with a destination vertex and weights for traveling
      alone or carpooling.
    """
    def __init__(self, dest: 'Vertex', weight_alone: int, weight_carpool: int):
        """
        This is a constructor for a class that initializes the destination vertex, weight for traveling
        alone, and weight for carpooling.
        
        :param dest: The destination vertex that this edge connects to
        :type dest: 'Vertex'
        :param weight_alone: The weight of traveling to the destination alone, without carpooling
        :type weight_alone: int
        :param weight_carpool: The weight_carpool parameter is an integer that represents the weight
        cost of carpooling to the destination vertex. 
        :type weight_carpool: int
        """
        self.dest = dest
        self.weight_alone = weight_alone
        self.weight_carpool = weight_carpool
    
    def __str__(self) -> str:
        output = "dest = " +  str(self.dest)
        return output

def optimalRoute(start: int, end: int, passengers: list, graph:list):
    """
    The function "optimalRoute" takes in a starting point, an ending point, a list of passengers, and a
    graph, and returns the optimal route for the passengers to travel from the starting point to the
    ending point.

    Approach description: 
    What the algorithm does here is to do dijkstra normally using the non-carpool lane as the weight
    and if it finds a passenger in the current vertex it will save the current path [start -> passenger] and it finds
    the path of [passenger -> end] by calling the 'tail' function which is essentially the same as optimal route but it uses
    the carpool lane as the weight

    
    :param start: The starting point of the journey
    :param end: The destination node or location for the passengers to reach
    :param passengers: It seems like the parameter "passengers" is missing some information. Can you
    provide more context or code for me to understand what it represents?
    :param graph: The graph parameter is data structure that represents a network of nodes and it includes the nodes's
    destination and the weight of alone lanes and carpool lanes from the source to the destination

    Time complexity = 
    O(|R| log |L|) 
        (I believe this, since in the worst case scenario (there are passengers) my dijkstra would run two versions 
        which is (alone dijkstra + carpool dijkstra) no matter how big the input)
    Aux sapce complexity =
    O(|L|+|R|) (caused by the algorithm using a distances and predecessor array as big as the graph)
    """

    graph = Graph(graph)
    def tail(vertex: int, end:int, graph: 'Graph'):
        """
        This healper function takes in a starting vertex, an ending vertex, and a graph and returns the shortest
        path between the two vertices.

        Approach description:
        it's the same as the 'optimalRoute' in terms of dijkstra but it uses the carpool weight since the tail function is only
        called when there is a passenger in the car
        
        :param vertex: The starting vertex of the path we want to find
        :type vertex: int
        :param end: The `end` parameter is an integer representing the vertex that we want to reach in
        the graph. It is used in the `tail` function to determine if we have reached the end vertex
        while traversing the graph
        :type end: int
        :param graph: The `graph` parameter is an instance of the `Graph` class, which represents a
        graph data structure. It contains information about the vertices and edges in the graph, as well
        as methods for manipulating graph
        :type graph: 'Graph'

        Time complexity = 
            O(|R| log |L|)
        Aux sapce complexity =
            O(|L|+|R|)
        """
        init = start
        distances = [float('inf')] * len(graph)
        distances[init] = 0
        
        priority_queue = MinHeap()
        priority_queue.insert((0,init))
        predecessors = [None] * len(graph)
        
        while len(priority_queue.array):
            dist, vertex = priority_queue.serve()
            if vertex == end:
                
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = predecessors[vertex]
                return list(reversed(path))
            
            for neighbour in graph.vertices[vertex].edges:
                new_distance = dist + neighbour.weight_carpool
                if distances[neighbour.dest.id] > new_distance:
                    distances[neighbour.dest.id] = new_distance
                    predecessors[neighbour.dest.id] = vertex
                    priority_queue.insert((new_distance, neighbour.dest.id))
                    

    distances = [float('inf')] * len(graph)
    distances[start] = 0
    
    priority_queue = MinHeap()
    priority_queue.insert((0,start))

    predecessors = [None] * len(graph)
    while priority_queue:
    
        dist, vertex = priority_queue.serve()
        if vertex == end:
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = predecessors[vertex]
                return list(reversed(path))
        
        for neighbour in graph.vertices[vertex].edges:
            new_distance = dist + neighbour.weight_alone
            if distances[neighbour.dest.id] > new_distance:
                distances[neighbour.dest.id] = new_distance
                predecessors[neighbour.dest.id] = vertex
                priority_queue.insert((new_distance, neighbour.dest.id))

        if vertex in passengers: 
                tail_lst = tail(vertex, end, graph)
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = predecessors[vertex]
                path = list(reversed(path))
                output = []
                if path[-1] == tail_lst[0]:
                    path.pop()
                if len(path) == 0:
                    return tail_lst
                if graph.has_way_to(graph.vertices[path[-1]], graph.vertices[tail_lst[0]]):
                    output =  path + tail_lst
                else:
                    output = tail_lst
                return output 
