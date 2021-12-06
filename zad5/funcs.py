image_filename = "zad4_graph.png"

def draw_graph(graph, start_vertex):
    import networkx as nx
    import matplotlib.pyplot as plt

    color_map = ["red" if v == start_vertex else "dodgerblue" for v in graph.vertexes]

    G = nx.DiGraph()
    G.add_nodes_from(graph.vertexes)
    G.add_weighted_edges_from(graph.edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=color_map, with_labels=True)

    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=13, font_weight='bold')

    plt.savefig(image_filename)

    from PIL import Image
    im = Image.open(image_filename)
    im.show()

from os import system
def clear_screen():
    system("cls||clear")

