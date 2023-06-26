
# REFERENCE: https://www.scaler.com/topics/dfs-python/

# code with start node to goal node
# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/depth-first-search-dfs-algorithm/ 

"""
TO DO
 [] get input from user
 [] start node and goal node (kase we need to find the optimal find to start node to goal node)
 [] showcase the existing graph
 [] edit the existing nodes
 [] terminate the code to exit
"""


def dfs(node, graph, visited, component):
    component.append(node)  # Store answer
    visited[node] = True  # Mark visited

    # Traverse to each adjacent node of a node
    for child in graph[node]:
        if not visited[child]:  # Check whether the node is visited or not
            dfs(child, graph, visited, component)  # Call the dfs recursively


if __name__ == "__main__":

    # Graph of nodes
    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    node = 0  # Starting node
    visited = [False]*len(graph)  # Make all nodes to False initially
    component = []
    dfs(node, graph, visited, component)  # Traverse to each node of a graph
    print(f"Following is the Depth-first search: {component}")  # Print the answer