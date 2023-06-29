
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
 [ ] edit the existing nodes
 [x] terminate the code to exit
"""

class Graph:
    # initializing
    def __init__(self):
        self.graph = {}

    # dfs traversal
    # entry point for dfs traversal
    def dfs(self, start_node, goal_node):
        visited = []  # initializes a set for the visited nodes
        found = self.visited(start_node, goal_node, visited)  # calls visited function
        for i in range(len(visited)):
            print(list(visited)[i], end=' ')
            if i != len(visited)-1:
                print("->", end=' ')
        print("\n\nFound the goal node \"" + goal_node + "\"")
        if not found:
            print("\nGoal node was not found.")

    # visited function
    # adds the current node to the visited set to mark that node as "visited" (also serves as the path)
    def visited(self, node, goal_node, visited, found_goal):
        visited.append(node)

        if node == goal_node:  # Check if the current node is the goal node
            return True
        else:
            found_goal = False
        # if the node has a child, it checks if it's in the visited set,
        # if not, it will call the visited function and pass the child to the visited set
        if node in self.graph:
            for child in self.graph[node]:
                if child not in visited and not found_goal:
                    found_goal = self.visited(child, goal_node, visited)
        return found_goal
 
    # adds the child of a parent node
    def add_child(self, parent_node, child_node, position=None):
        if parent_node not in self.graph:
            self.graph[parent_node] = []
        children = self.graph[parent_node]
        
        if type(position) != int:
            children.append(child_node)  # Append child node at the end if position is not specified
        else:
            children.insert(position, child_node)  # Insert child node at the specified position
        
        self.graph[parent_node] = children

    # prints the current graph
    def print_current_graph(self):
        for parent_node, children in self.graph.items():
            print(f"{parent_node} -> {', '.join(children)}")

    def menu(self):
        print("[a] Input nodes")
        print("[b] See current graph")
        print("[c] DFS Search")
        print("[d] Exit the program")
        option = input("\nEnter your option: ")
        while option != "d":
            if option == "a":
                parent_node = input("\nEnter parent node: ")
                child_node = input("Enter child node: ")
                position = input("Enter the position to insert the child node (optional): ")
                if position:
                    position = int(position)
                dfs_graph.add_child(parent_node, child_node, position)
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
            print("[a] Input nodes")
            print("[b] See current graph")
            print("[c] DFS Search")
            print("[d] Exit the program")
            option = input("\nEnter your option: ")


if __name__ == "__main__":
    dfs_graph = Graph()

    dfs_graph.menu()

    print("Terminating code. Goodbye!")

