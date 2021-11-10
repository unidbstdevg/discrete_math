import funcs as f
from graph import *

is_graph_oriented = False
while True:
    ans = input("Should graph be oriented? [Y/n] ")
    if ans == "y" or ans == "Y" or ans == "":
        is_graph_oriented = True
        break
    elif ans == "n" or ans == "N":
        is_graph_oriented = False
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

graph = Graph(is_graph_oriented)

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
        print("[error] Edge is two vertices separted by space. Example: A B")
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

print("Vertexes:", *sorted(graph.vertexes))
print("Edges:", *sorted(graph.edges))
