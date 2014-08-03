# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph_edges):
    # Convert from list of edges to dictionary representing graph
    graph = construct_graph(graph_edges)
    
    no_of_odd_nodes = count_odd_nodes(graph)
    
    # For a path to be possible num of odd nodes should either be 2 or 0
    if no_of_odd_nodes not in (2, 0):
            # No path possible
            return None
    
    # At this point, a eulerian path is possible
    start_node = get_start_node(graph, no_of_odd_nodes)
    
    stack = []
    tour = []
    current_node = start_node
    while (has_neighbors(current_node, graph) or len(stack) != 0):
        # Continue loop until current_node has no neighbors AND stack is empty
        if not has_neighbors(current_node, graph):
            # Add node to the tour and set current node to the one popped from
            # stack
            tour.append(current_node)
            current_node = stack.pop()
            continue
        else:
            # Add current node to stack
            # Pick any of its neighbors
            # Remove edge between current_node and that neighbor
            # Set the neighbor to be new current_node
            stack.append(current_node)
            neighbor = get_any_neighbor(current_node, graph)
            remove_edge(current_node, neighbor, graph)
            current_node = neighbor
    
    # current_node is the last node in path. Add it to tour.
    tour.append(current_node)
    # The tour is in reverse order compared to the start node we chose
    tour.reverse()
    return tour

"""
Function that takes in a list of edges represented as list of edges and convert
it into a graph represented by a dictionary.
"""
def construct_graph(edges):
    graph = {}
    for x, y in edges:
        if x not in graph:
            graph[x] = [y]
        else:
            graph[x].append(y)
        if y not in graph:
            graph[y] = [x]
        else:
            graph[y].append(x)
    return graph

"""
Count number of nodes with odd degree in the graph
"""
def count_odd_nodes(graph):
    no_of_odd_nodes = 0
    for connections in graph.values():
        degree = len(connections)
        if degree % 2 == 1:
            no_of_odd_nodes += 1
    return no_of_odd_nodes

"""
Get a node that is a viable node to serve as start node of a eulerian path
"""
def get_start_node(graph, no_of_odd_nodes):
    if no_of_odd_nodes == 2:
        # Need to start at a odd node
        for node in graph:
            if len(graph[node]) % 2 == 1:
                return node
    else:
        # Can start from any node
        return graph.keys()[0]

"""
Check if the node in graph has neighbors
"""
def has_neighbors(node, graph):
    if len(graph[node]) == 0: return False
    else: return True

"""
Return any of the available neighbors of the node in the graph
"""
def get_any_neighbor(node, graph):
    return graph[node][0]

"""
Remove an edge of the graph between node1 and node2
"""
def remove_edge(node1, node2, graph):
    graph[node1].remove(node2)
    graph[node2].remove(node1)

def test():
    # Test
    input_graph = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (5, 3), (1, 3)]
    tour = find_eulerian_tour(input_graph)
    print tour
    input_graph = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
    tour = find_eulerian_tour(input_graph)
    print tour
    input_graph = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)]
    tour = find_eulerian_tour(input_graph)
    print tour
    input_graph = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 4)]
    tour = find_eulerian_tour(input_graph)
    print tour
    input_graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    tour = find_eulerian_tour(input_graph)
    print tour

