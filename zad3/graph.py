class Graph:
    def __init__(self, is_oriented):
        self.is_oriented = is_oriented

        self.edges = set()
        self.vertexes = set()

    def add_edge(self, edge):
        if len(edge) != 2:
            raise ExceptionEdgeWrongFormat

        if not self.is_oriented:
            edge = tuple(sorted(edge))

        if edge in self.edges:
            raise ExceptionDuplicateEdge

        self.edges.add(edge)
        self.vertexes.update(edge)

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


class ExceptionEdgeWrongFormat(Exception):
    pass
class ExceptionDuplicateEdge(Exception):
    pass
class ExceptionNoMoreExtend(Exception):
    pass

