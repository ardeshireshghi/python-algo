class Graph(object):
    def __init__(self, nodes=1, edges=0):
        self.edges = edges
        self.edges_list = []
        self.set_vertices(nodes)

    def set_vertices(self, nodes):
        self.vertices = nodes
        self._adj_list = [[] for _ in range(0, self.vertices)]

    def set_edges(self, edges):
        self.edges = edges

    def add_edge(self, edge):
        if edge[0] == edge[1] or len(self.edges_list) == self.edges:
            return

        self.edges_list.append(edge)
        self._adj_list[edge[0]].append(edge[1])
        self._adj_list[edge[1]].append(edge[0])

    def get_adj_list(self):
        return self._adj_list
