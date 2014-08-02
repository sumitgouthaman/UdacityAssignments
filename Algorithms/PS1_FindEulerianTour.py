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

def find_eulerian_tour(graph):
    nodes = {}
    for x, y in graph:
        if x not in nodes:
            nodes[x] = [y]
        else:
            nodes[x].append(y)
        if y not in nodes:
            nodes[y] = [x]
        else:
            nodes[y].append(x)
    
    no_of_odd_nodes = 0
    for connections in nodes.values():
        degree = len(connections)
        if degree % 2 == 1:
            no_of_odd_nodes += 1
            
    if no_of_odd_nodes != 2:
        if no_of_odd_nodes != 0:
            # No path possible
            return None
    
    # At this point, a eulerian path is possible
    start_node = None;
    end_node = None;
    if no_of_odd_nodes == 2:
        # Need to start at a odd node
        for node in nodes:
            if len(nodes[node]) % 2 == 1:
                if start_node == None:
                    start_node = node
                else:
                    end_node = node
                    break
    else:
        # Can start from any node
        start_node = nodes.keys()[0]
        end_node = nodes.keys()[0]
    
    visit_order = []
    degree_of_end_node = len(nodes[end_node])
    
    while len(graph) > 0:
        (x, y) = graph.pop(0)
        print x, y
        if x != start_node and y!=start_node:
            graph.append((x, y))
            continue
            
        if (x == start_node and y == end_node) or (y == start_node and x == end_node):
            if y == start_node:
                x, y = y, x
            
            if degree_of_end_node > 1 or len(graph) == 0:
                degree_of_end_node -= 1
                visit_order.append((x, y))
                start_node = y
            else:
                graph.append((x, y))
            
            continue
            
        if y == start_node:
            x, y = y, x
        visit_order.append((x, y))
        start_node = y
              
    tour = [i for i, j in visit_order]
    tour.append(visit_order[-1][1])
    return tour

if __name__ == "__main__":
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
    