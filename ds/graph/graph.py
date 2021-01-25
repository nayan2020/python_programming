class Vertex:
    def __init__(self, key):
        self._key = key
        self._neighbour = set()

    def add_neighbour(self, neighbour):
        self._neighbour.add(neighbour)

    def get_key(self):
        return self._key

    def get_neighbour(self):
        return self._neighbour

    def __str__(self):
        s = str(self.get_key())
        s += ":{"
        for i in self._neighbour:
            s += str(i.get_key()) + ","
        if s[-1] == ",":
            s = s[:-1]
        s += "}"
        return s


class UndirectedGraph:
    def __init__(self):
        self._vertics = dict()

    def add_vertex(self, vertex):
        self._vertics[vertex] = Vertex(vertex)

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self._vertics:
            self.add_vertex(from_vertex)
        if to_vertex not in self._vertics:
            self.add_vertex(to_vertex)

        self._vertics[from_vertex].add_neighbour(self._vertics[to_vertex])

        self._vertics[to_vertex].add_neighbour(self._vertics[from_vertex])

    def get_vertex(self, vertex):
        return self._vertics.get(vertex, None)

    def get_vertics(self):
        return list(self._vertics.keys())

    def get_edges(self):
        lst = []
        for src_vertex in self._vertics:
            src_vertex_obj = self._vertics[src_vertex]
            for vertex in src_vertex_obj.get_neighbour():
                lst.append((src_vertex, vertex.get_key()))

        return lst

    def get_degree(self, vertex):
        return len(self._vertics[vertex].get_neighbour())


def main():
    nodes = {
        0: [1, 2, 5, 6],
        1: [],
        2: [],
        3: [4, 5],
        4: [6],
        5: [],
        6: [],
        7: [8],
        8: [],
        9: [10, 11, 12],
        10: [],
        11: [12],
        12: []
    }
    undirectedgraph = UndirectedGraph()
    for i in nodes:
        undirectedgraph.add_vertex(i)

    for i in nodes:
        k = nodes[i]
        for j in k:
            undirectedgraph.add_edge(i, j)

    print(f"vertices: {undirectedgraph.get_vertics()}")
    print("Edges: ")
    for i in undirectedgraph.get_edges():
        print(f"{i}", end=", ")
    print()
    for i in undirectedgraph.get_vertics():
        print(f'vertex is: {i:2d} degree: {undirectedgraph.get_degree(i)}')

    print(type(undirectedgraph.get_vertex(0)))


if __name__ == '__main__':
    main()
