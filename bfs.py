# Python code to implement breadth-first graph search algorithm.

from collections import defaultdict

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list)

    def add_edge(self, vertex1, vertex2): 
        self.graph[vertex1].append(vertex2)
    
    def BFS(self, source_vertex): 
        graphlen = len(self.graph)
        visited_vertices = [False] * (graphlen)

        BFS_queue = []

        BFS_queue.append(source_vertex)
        visited_vertices[source_vertex] = True

        while BFS_queue: 

            source_vertex = BFS_queue.pop(0)

            print(source_vertex, end=" ")

            for neighbor in self.graph[source_vertex]: 
                if visited_vertices[neighbor] == False:
                    BFS_queue.append(neighbor)
                    visited_vertices[neighbor] = True