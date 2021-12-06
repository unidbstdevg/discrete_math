import funcs as f
from graph import *

print("Dijkstra’s algorithm for directed weighted graph")

power = -1
while True:
    ans = input("Count of vertexes in graph: ")
    try:
        power = int(ans)
        break
    except ValueError:
        print("[error] Please type number")
        continue

graph = Graph()

edges_print_buf = ""
while True:
    f.clear_screen()
    print("Edge from A to B with weight=4: A B 4")
    print("Current list of edges:")
    print(edges_print_buf)

    print("Type list of edges, one per line. Vertexes separated by space. (Pass empty line to finish)")
    line = input()
    if(line == ""):
        break

    edge = tuple(line.split())
    try:
        graph.add_edge(edge)
        edges_print_buf += line + "\n"
    except ExceptionEdgeWrongFormat:
        print("[error] Edge is two vertices and weight(positive number) separated by space. Example: A B 4")
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

print()
while True:
    ans = input("Do you want visualize graph? [Y/n] ")
    if ans == "y" or ans == "Y" or ans == "":
        print("Drawing... Please wait".format(f.image_filename))
        f.draw_graph(graph, start)
        print("See file '{}' if not opened automatically".format(f.image_filename))
        input("(Press enter to continue)")
        break
    elif ans == "n" or ans == "N":
        break
    else:
        print("Please type y or n")
        continue

