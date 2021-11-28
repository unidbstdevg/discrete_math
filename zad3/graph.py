class Graph:
    def __init__(self, is_directed):
        self.is_directed = is_directed

        self.edges = set()
        self.vertexes = set()

    def add_edge(self, edge):
        if len(edge) != 2:
            raise ExceptionEdgeWrongFormat

        if edge in self.edges:
            raise ExceptionDuplicateEdge

        self.vertexes.update(edge)

        if self.is_directed:
            self.edges.add(edge)
            return
        else:
            edge = tuple(sorted(edge, reverse=False))
            self.edges.add(edge)
            edge = tuple(sorted(edge, reverse=True))
            self.edges.add(edge)

    def power(self):
        return len(self.vertexes)

    def extend_to(self, new_power):
        if self.power() >= new_power:
            raise ExceptionNoMoreExtend

        new_vertexes = []

        count_new_vertexes = new_power - self.power()
        for i in range(1, count_new_vertexes + 1):
            i = str(i)

            while i in self.vertexes:
                i = "N" + i

            self.vertexes.add(i)
            new_vertexes.append(i)

        assert len(new_vertexes) == count_new_vertexes, \
                "count of new vertexes not equal length of list of new vertexes"
        assert new_power == self.power(), \
                "new_power not equal self.power"

        return new_vertexes

    def loops_count(self):
        r = 0
        for edge in self.edges:
            if edge[0] == edge[1]:
                r += 1

        return r

    def print_adjacency_matrix(self):
        sorted_vertexes = sorted(self.vertexes)

        # header - columns names
        print(" ", end=" ")
        for v in sorted_vertexes:
            print(Colors.black_on_white + v + Colors.restore, end=" ")
        print()

        for v in sorted_vertexes:
            # header - row name
            print(Colors.black_on_white + v + Colors.restore, end=" ")

            for other_v in sorted_vertexes:
                if self.is_directed:
                    # TODO: is right edge, maybe (other_v, v) ?
                    if (v, other_v) in self.edges:
                        print(1, end=" ")
                        continue
                else:
                    if (v, other_v) in self.edges or (other_v, v) in self.edges:
                        print(1, end=" ")
                        continue
                print(0, end=" ")

            print()

    def print_incidences_list(self):
        sorted_vertexes = sorted(self.vertexes)
        for v in sorted_vertexes:
            # header - row name
            print(Colors.black_on_white + v + Colors.restore, end=": ")

            for other_v in sorted_vertexes:
                if self.is_directed:
                    if (v, other_v) in self.edges:
                        print(other_v, end=" ")
                else:
                    if (v, other_v) in self.edges or (other_v, v) in self.edges:
                        print(other_v, end=" ")
            print()

    # return:
    #       for directed: list: [outcome, income]
    #       for undirected: number
    def max_vertex_degree(self):
        mc = 0 if not self.is_directed else [0, 0]
        for v in self.vertexes:
            c = 0 if not self.is_directed else [0, 0]
            for edge in self.edges:
                if v not in edge:
                    continue

                if not self.is_directed:
                    # for undirected we check only first vertex in edge, because there is always pairs like (a,b) and (b,a)
                    if edge[0] == v:
                        c += 1
                        # for undirected: 1 loop counts as 2 degree
                        if edge[0] == edge[1]:
                            c += 1
                else:
                    if edge[0] == v:
                        c[0] += 1
                    if edge[1] == v:
                        c[1] += 1

            if not self.is_directed:
                mc = max(mc, c)
            else:
                mc[0] = max(mc[0], c[0])
                mc[1] = max(mc[1], c[1])

        return mc


class ExceptionEdgeWrongFormat(Exception):
    pass
class ExceptionDuplicateEdge(Exception):
    pass
class ExceptionNoMoreExtend(Exception):
    pass

class Colors:
    restore = "\033[0m"
    black_on_white = "\033[30m\033[47m"
    highlight = "\033[41m"
