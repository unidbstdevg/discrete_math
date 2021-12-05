image_filename = "zad4_graph.png"

def draw_graph(graph, start_vertex):
    import networkx as nx
    import matplotlib.pyplot as plt

    color_map = ["red" if v == start_vertex else "green" for v in graph.vertexes]

    G = nx.DiGraph() if graph.is_directed else nx.Graph()
    G.add_nodes_from(graph.vertexes)
    G.add_edges_from(graph.edges)

    nx.draw(G, node_color=color_map, with_labels=True)
    plt.savefig(image_filename)

    from PIL import Image
    im = Image.open(image_filename)
    im.show()

from os import system
def clear_screen():
    system("cls||clear")

