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

    # def traverse(self, result_pathes, start, cur_path=[]):
    #     cur_path.append(start)

    #     pathes = self.find_pathes_from(start)
    #     pathes -= set(cur_path)

    #     if len(pathes) == 0:
    #         result_pathes.append(cur_path)
    #         return

    #     for p in pathes:
    #         new_path = cur_path.copy()

    #         self.traverse(result_pathes, p, new_path)

    # def find_pathes_from(self, v):
    #     pathes = set()
    #     for edge in self.edges:
    #         # we drop loops to prevent infinity loop when going through this path
    #         if edge[0] == v and edge[1] != v:
    #             pathes.add(edge[1])

    #     return pathes

    # def traverse_visit(self, start, visited):
    #     pathes = self.find_pathes_from(start)
    #     pathes -= visited
    #     for p in pathes:
    #         visited.add(p)
    #         self.traverse_visit(p, visited)

class ExceptionEdgeWrongFormat(Exception):
    pass
class ExceptionDuplicateEdge(Exception):
    pass
class ExceptionNoMoreExtend(Exception):
    pass
