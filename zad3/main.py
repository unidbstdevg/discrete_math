import funcs as f
from graph import *

is_graph_directed = False
while True:
    ans = input("Should graph be directed? [Y/n] ")
    if ans == "y" or ans == "Y" or ans == "":
        is_graph_directed = True
        break
    elif ans == "n" or ans == "N":
        is_graph_directed = False
        break
    else:
        print("Please type y or n")
        continue

power = -1
while True:
    ans = input("Count of vertexes in graph: ")
    try:
        power = int(ans)
        break
    except ValueError:
        print("[error] Please type number")
        continue

graph = Graph(is_graph_directed)

edges_print_buf = ""
while True:
    f.clear_screen()
    print("Current list of edges:")
    print(edges_print_buf)

    print("Type list of edges, one per line. Vertexes separated by space. (Pass empty line to finish)")
    line = input()
    if(line == ""):
        break

    vertexes = tuple(line.split())
    try:
        graph.add_edge(vertexes)
        edges_print_buf += vertexes[0] + " " + vertexes[1] + "\n"
    except ExceptionEdgeWrongFormat:
        print("[error] Edge is two vertices separated by space. Example: A B")
        input("(Press enter to continue)")
        continue
    except ExceptionDuplicateEdge:
        print("[error] This edge is already in graph")
        input("(Press enter to continue)")
        continue

try:
    new_vertexes = graph.extend_to(power)
    print("Added new disconnected vertexes to match user defined count of vertexes:", *sorted(new_vertexes))
except ExceptionNoMoreExtend:
    if graph.power() > power:
        print("[warning] You've typed more vertexes than previously typed count of vertexes")
        input("(Press enter to continue)")

print("\n" + ("Directed" if is_graph_directed else "Undirected") + " graph")
print("Vertexes(count={}):".format(graph.power()), *sorted(graph.vertexes))
print("Edges(count={}):".format(len(graph.edges)), *sorted(graph.edges))
print("Loops count =", graph.loops_count())
print("Max vertex power =", graph.max_vertex_power())

print("\nAdjacency matrix (smejnost'):")
graph.print_adjacency_matrix()

print("\nList of incidences:")
graph.print_incidences_list()

