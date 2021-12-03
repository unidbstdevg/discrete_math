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

    def traverse(self, result_pathes, start, cur_path=[]):
        cur_path.append(start)

        pathes = self.find_pathes_from(start)
        pathes -= set(cur_path)

        if len(pathes) == 0:
            result_pathes.append(cur_path)
            return

        for p in pathes:
            new_path = cur_path.copy()

            self.traverse(result_pathes, p, new_path)

    def find_pathes_from(self, v):
        pathes = set()
        for edge in self.edges:
            # we drop loops to prevent infinity loop when going through this path
            if edge[0] == v and edge[1] != v:
                pathes.add(edge[1])

        return pathes

    def test_hamiltonian(self):
        print("TODO: diagnostic test_hamiltonian")
        return True

    def find_hamiltonian_cycles(self, start_v):
        pathes = []
        self.traverse(pathes, start_v)

        # drop not cycles
        pathes = list(filter(lambda p: p[0] in self.find_pathes_from(p[-1]), pathes))

        # drop all pathes in which not all vertexes are used
        graph_vertexes_len = len(self.vertexes)
        pathes = list(filter(lambda p: len(p) == graph_vertexes_len, pathes))

        return pathes

class ExceptionEdgeWrongFormat(Exception):
    pass
class ExceptionDuplicateEdge(Exception):
    pass
class ExceptionNoMoreExtend(Exception):
    pass
