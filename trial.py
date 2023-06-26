class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()
        self._dfs_util(start_node, visited)

    def _dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        
        if node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self._dfs_util(neighbor, visited)

    def print_adjacency_list(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {', '.join(neighbors)}")


# Create a graph based on user input
graph = Graph()

while True:
    u = input("Enter source vertex (or 'q' to quit): ")
    if u == 'q':
        break

    v = input("Enter destination vertex: ")
    graph.add_edge(u, v)

start_node = input("Enter the starting node for DFS: ")

# Print the adjacency list
print("Adjacency List:")
graph.print_adjacency_list()

# Perform DFS on the graph
print("DFS traversal:")
graph.dfs(start_node)