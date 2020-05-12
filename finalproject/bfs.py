# Python code to implement breadth-first graph search algorithm.

'''
We use the defaultdict class over the dict class. 
This is because default dict will default a value for a key that has not been set yet. 
If we used dict, we would have to include additional checks to ensure the key exists, and if it didn't, set the key to what we wanted. 
'''

from collections import defaultdict

class Graph: 

    # Init contructor.
    def __init__(self): 

        # Store graph in dictionary. 
        self.graph = defaultdict(list)

    # Function to add an edge to the graph, given a start vertex and an end vertex. 
    def add_edge(self, vertex1, vertex2): 
        self.graph[vertex1].append(vertex2)
    
    # Function to perform bfs. 
    def BFS(self, source_vertex): 

        graphlen = len(self.graph)
        
        # Keeps track of vertices that have already been visited. 
        # Initially all vertices are set to false [aka not visited]. 
        visited_vertices = [False] * (graphlen)

        # Store vertices in a queue -- this will serve as our adjacency list. 
        BFS_queue = []

        # Begin by adding specified source ("start") vertex to the adjacency list [and mark it as visited]. 
        BFS_queue.append(source_vertex)
        visited_vertices[source_vertex] = True

        # Go through every vertex by processing vertices in adjancency list. 
        while BFS_queue: 

            # Dequeue vertex at the beginning of list. 
            source_vertex = BFS_queue.pop(0)

            # Print vertex being processed. 
            print(source_vertex, end=" ")

            # Add all adjacent vertices that have not been visited yet to the queue. 
            # Once enqueued, mark said vertex as visited.
            for neighbor in self.graph[source_vertex]:
                if visited_vertices[neighbor] == False:
                    BFS_queue.append(neighbor)
                    visited_vertices[neighbor] = True