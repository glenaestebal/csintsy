
# REFERENCE: https://www.scaler.com/topics/dfs-python/

# code with start node to goal node
# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/depth-first-search-dfs-algorithm/ 


"""
TO DO
 legend: [x] done || [/] not sure kung tama ba

 [x] get input from user
 [x] start node
 [] goal node (kase we need to find the optimal find to start node to goal node)
 [x] showcase the existing graph
 [] edit the existing nodes
 [/] terminate the code to exit
"""


class Graph:
    def __init__(self):
        self.graph = {}

    def dfs(self, node):
        visited = set()
        self.visited(start_node, visited)

    def visited(self, node, visited):
        visited.add(node)
        print(node, end=' ')

        if node in self.graph:
            for child in self.graph[node]:
                if child not in visited:
                    self.visited(child, visited)

    def add_child(self, parent_node, child_node):
        if parent_node not in self.graph:
            self.graph[parent_node] = []
        self.graph[parent_node].append(child_node)
    
    def print_adjacency_list(self):
        for parent_node, children in self.graph.items():
            print(f"{parent_node}: {', '.join(children)}")


if __name__ == "__main__":

    # Graph of nodes
    # graph = {
    #     0: [2],
    #     1: [2, 3],
    #     2: [0, 1, 4],
    #     3: [1, 4],
    #     4: [2, 3]
    # }

    dfs_graph = Graph()

    while True:
        parent_node = input("Enter parent node (or 'x' to quit): ")
        if parent_node == "x":
            break

        child_node = input("Enter child node: ")
        dfs_graph.add_child(parent_node, child_node)

        print("\nCurrent Graph: ")
        dfs_graph.print_adjacency_list()
        print("\n") 

    start_node = input("\nEnter the start node for DFS traversal: ")

    print("\nFollowing is the Depth-first search: ")
    dfs_graph.dfs(start_node)