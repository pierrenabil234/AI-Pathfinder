import networkx as nx
import matplotlib.pyplot as plt

def valid_neighbors(m, r, c, current_node, G):
    node1 = (r + 1, c)
    node2 = (r - 1, c)
    node3 = (r, c + 1)
    node4 = (r, c - 1)

    if r > 0 and r < len(m) - 1 and m[r + 1][c] != 1 and m[r - 1][c] != 1:
        G.add_edge(current_node, node1)
        G.add_edge(current_node, node2)
    elif r > 0 and m[r - 1][c] != 1:
        G.add_edge(current_node, node2)
    elif r < len(m) - 1 and m[r + 1][c] != 1:
        G.add_edge(current_node, node1)

    if c > 0 and c < len(m[0]) - 1 and m[r][c + 1] != 1 and m[r][c - 1] != 1:
        G.add_edge(current_node, node3)
        G.add_edge(current_node, node4)
    elif c > 0 and m[r][c - 1] != 1:
        G.add_edge(current_node, node4)
    elif c < len(m[0]) - 1 and m[r][c + 1] != 1:
        G.add_edge(current_node, node3)

def matrix(m):
    end_nodes = []
    G = nx.Graph()

    for r in range(len(m)):
        for c in range(len(m[0])):
            current_node = (r, c)

            if m[r][c] == 2:
                start_node = current_node
                
            if m[r][c] == 3:
                end_node = current_node
                end_nodes.append(end_node)

            if m[r][c] != 1:
                valid_neighbors(m, r, c, current_node, G)
    #alwan=['red' if node==start_node else 'green' for node in G.nodes ]
    
    #alwan = ['red' if node == start_node else 'blue' if node == end_node else 'green' for node in G.nodes]
    #alwan = ['red' if node == start_node else 'blue' if node == end_node for end_node in G.nodes else 'green' for node in G.nodes]
    alwan =  ['green' if node == start_node else 'red' if node in end_nodes else 'yellow' for node in G.nodes]
    pos = {(r, c): (c, -r) for r in range(len(m)) for c in range(len(m[0])) if m[r][c] != 1}
    
    nx.draw(G, pos,node_color=alwan, with_labels=True)
    #plt.show()
    return G,start_node,end_nodes