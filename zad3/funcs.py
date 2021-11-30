image_filename = "zad3_graph.png"

def draw_graph(graph):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph() if graph.is_directed else nx.Graph()
    G.add_edges_from(graph.edges)
    G.add_nodes_from(graph.vertexes)

    nx.draw(G, with_labels=True)
    plt.savefig(image_filename)

    from PIL import Image
    im = Image.open(image_filename)
    im.show()

from os import system
def clear_screen():
    system("cls||clear")

