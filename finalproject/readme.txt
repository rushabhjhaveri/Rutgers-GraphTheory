There are two code files in this project: 
- bfs.py
- bfsdriver.py

To run the program, run bfsdriver.py [driver code]. The driver has been pre-filled with an initialized graph and added edges. 

If you wish to run this algorithm with your own graph, add edges between two vertices by using graph.add_edge(vertex1, vertex2) as done in the driver. 

Call the bfs algorithm by using graph.BFS(source_vertex), where source_vertex is the initial vertex you wish to run BFS on. 

Once ready to run the code, run as follows: 

python3 bfsdriver.py

Make sure you are in the finalproject folder as that is where the code files are located; otherwise the code will not run. 

Sample output [for current graph]: 

Shortest path:
2 0 3 1

This represents the shortest path from the source vertex covering all vertices in the graph. 