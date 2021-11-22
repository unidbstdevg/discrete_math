def draw_graph(graph):
    import networkx as nx
    from networkx.drawing.nx_agraph import to_agraph

    G = nx.DiGraph() if graph.is_directed else nx.Graph()
    G.add_edges_from(graph.edges)
    G.add_nodes_from(graph.vertexes)

    nx.draw_circular(G)

    A = to_agraph(G)
    A.layout("dot")
    A.draw("zad3_graph.png")

    from PIL import Image
    im = Image.open("zad3_graph.png")
    im.show()

    # from os import system
    # system("feh zad3_graph.png")


def clear_screen():
    from os import system
    system("cls||clear")
