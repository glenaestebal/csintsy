
# REFERENCES

# https://www.scaler.com/topics/dfs-python/
# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/depth-first-search-dfs-algorithm/ 
# https://stackoverflow.com/questions/70550888/how-i-can-stop-depth-first-search-at-specific-node

"""
TO DO
 legend: [x] done || [/] not sure kung tama ba

 [x] get input from user
 [x] start node
 [x] goal node (kase we need to find the optimal find to start node to goal node)
 [x] showcase the existing graph
 [x] edit the existing nodes
 [x] terminate the code to exit
"""

class Graph:
    # initializing
    def __init__(self):
        self.graph = {}

    # dfs traversal
    # entry point for dfs traversal
    def dfs(self, start_node, goal_node):
        visited = set() # initializes a set for the visitetd nodes
        self.visited(start_node, visited) # calls visited function
        
    # visited function
    # adds the current node to the visited set to mark that node as "visited" (also serves as the path)
    def visited(self, node, visited):
        visited.add(node)
        print(node, end=' ')

        # if the node has a child, it check if its in the visited set,
        # if not, it will call the visited function and pass the child to the visited set
        if node in self.graph:
            for child in self.graph[node]:
                if child == goal_node:
                    print(goal_node, "\nFound the goal node!")
                elif child not in visited:
                    self.visited(child, visited)

    # adds the child of a parent node
    def add_child(self, parent_node, child_node):
        # if the parent node is not in the graph, it will be added there
        if parent_node not in self.graph:
            self.graph[parent_node] = []
        # else, the child_node is appended to the list of the parent node's children
        self.graph[parent_node].append(child_node)
    
    # prints the current graph
    def print_current_graph(self):
        for parent_node, children in self.graph.items():
            print(f"{parent_node}: {', '.join(children)}")

    def menu(self):
        print("[a] Input nodes")
        print("[b] See current graph")
        print("[c] DFS Search")
        print("[d] Exit the program")
        
if __name__ == "__main__":
    dfs_graph = Graph()
    
    dfs_graph.menu()
    option = input("\nEnter your option: ")
    while option!= "d":
        if option == "a":
            parent_node = input("\nEnter parent node: ")
            child_node = input("Enter child node: ")
            dfs_graph.add_child(parent_node, child_node)
        elif option == "b":
            print("\nCurrent Graph: ")
            dfs_graph.print_current_graph()
        elif option == "c":
            start_node = input("\nEnter the start node for DFS traversal: ")
            goal_node = input("\nEnter the goal node for DFS traversal: ")

            print("\nFollowing is the Depth-first search: ")
            dfs_graph.dfs(start_node, goal_node)
        else:
            print("Invalid option!")
        print()
        dfs_graph.menu()
        option = input("\nEnter your option: ")
        
    print("Terminating code. Goodbye!")

