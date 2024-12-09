class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v):
        # Adding edge for undirected graph
        if u < self.num_vertices and v < self.num_vertices:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else:
            print("Error: Vertex out of range")
    
    def display_graph(self):
        # Display the adjacency list of the graph
        for i in range(self.num_vertices):
            print(f"Vertex {i}: ", end="")
            for neighbor in self.adj_list[i]:
                print(neighbor, end=" ")
            print()
            
# Example usage:
num_vertices = 5  # Number of vertices in the graph
graph = Graph(num_vertices)

# Adding edges
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Display the graph
graph.display_graph()
