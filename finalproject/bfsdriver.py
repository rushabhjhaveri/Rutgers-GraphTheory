# Driver code to execute the BFS graph search algorithm (implemented in python). 
import bfs as bfs 

# Create a new graph.
graph = bfs.Graph()

# Add edges to this graph.
graph.add_edge(0, 1)

graph.add_edge(0, 2)

graph.add_edge(0, 3)

graph.add_edge(1, 2)

graph.add_edge(1, 3)

graph.add_edge(2, 0)

graph.add_edge(2, 3)

graph.add_edge(3, 3)

print("Shortest path:")

# Perform bfs on this graph. 
graph.BFS(2)