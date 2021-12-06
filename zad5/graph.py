class Graph:
    def __init__(self):
        self.edges = set()
        self.vertexes = set()

    def add_edge(self, edge):
        if len(edge) != 3:
            raise ExceptionEdgeWrongFormat
        try:
            weight = int(edge[2])
            if weight < 0:
                raise ExceptionEdgeWrongFormat
        except:
            raise ExceptionEdgeWrongFormat

        for e in self.edges:
            if e[0] == edge[0] and e[1] == edge[1]:
                raise ExceptionDuplicateEdge

        self.vertexes.add(edge[0])
        self.vertexes.add(edge[1])

        self.edges.add((edge[0], edge[1], weight))

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

    def dijkstra(self, start):
        res_lens = dict()
        res_pathes = dict()
        for v in self.vertexes:
            if v == start:
                res_lens[v] = 0
                res_pathes[v] = v
            else:
                res_lens[v] = float("inf")
                res_pathes[v] = "*unreachable*"

        unvisited = self.vertexes.copy()
        while True:
            if len(unvisited) == 0:
                break

            cur_v = min(unvisited, key=res_lens.get)
            cur_pathes = self.find_pathes_from(cur_v)

            for p in cur_pathes:
                l = res_lens[cur_v] + self.get_len_for_edge((cur_v, p))
                if l < res_lens[p]:
                    res_lens[p] = l
                    res_pathes[p] = res_pathes[cur_v] + " -> " + p

            unvisited.remove(cur_v)

        res = dict()
        for v in self.vertexes:
            res[v] = (res_lens[v], res_pathes[v])
        return res

    def get_len_for_edge(self, edge):
        for e in self.edges:
            if edge[0] == e[0] and edge[1] == e[1]:
                return e[2]

        raise ExceptionEdgeDoesNotExist

    def find_pathes_from(self, v):
        pathes = set()
        for edge in self.edges:
            # we drop loops to prevent infinity loop when going through this path
            if edge[0] == v and edge[1] != v:
                pathes.add(edge[1])

        return pathes

class ExceptionEdgeWrongFormat(Exception):
    pass
class ExceptionDuplicateEdge(Exception):
    pass
class ExceptionNoMoreExtend(Exception):
    pass
class ExceptionEdgeDoesNotExist(Exception):
    pass
