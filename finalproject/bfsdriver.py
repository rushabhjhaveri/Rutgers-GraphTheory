# Driver code to execute the BFS graph search algorithm (implemented in python). 
import bfs as bfs 

graph = bfs.Graph()

graph.add_edge(0, 1)

graph.add_edge(0, 2)

graph.add_edge(1, 2)

graph.add_edge(2, 0)

graph.add_edge(2, 3)

graph.add_edge(3, 3)

graph.BFS(2)