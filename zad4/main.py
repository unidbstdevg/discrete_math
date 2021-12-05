import funcs as f
from graph import *

print("Search for all Hamiltonian cycles in a graph (directed or undirected")

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

user_input_edges = []
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
        user_input_edges.append(vertexes)

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
    input("(Press enter to continue)")
    print()
except ExceptionNoMoreExtend:
    if graph.power() > power:
        print("[warning] You've typed more vertexes than previously typed count of vertexes")
        input("(Press enter to continue)")
        print()

print("Vertexes:", *graph.vertexes)
start = ""
while True:
    start = input("Vertex to start from: ")
    if start not in graph.vertexes:
        print("[error] Vertex '" + start + "' does not exist")
    else:
        break

if graph.test_possible_hamiltonian():
    cycles = graph.find_hamiltonian_cycles(start)

    if len(cycles) == 0:
        print("By the result of exhaustive search, there are no Hamiltonian cycles in the graph")
    else:
        print("Hamiltonian cycles:")
        for c in cycles:
            print(*c)
else:
    pass

print()
while True:
    ans = input("Do you want visualize graph? [Y/n] ")
    if ans == "y" or ans == "Y" or ans == "":
        print("Drawing... Please wait".format(f.image_filename))
        f.draw_graph(graph, start)
        input("(Press enter to continue)")
        break
    elif ans == "n" or ans == "N":
        break
    else:
        print("Please type y or n")
        continue

