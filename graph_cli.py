import re
from graph import Graph


class GraphAddEdgeCommand():
    def __init__(self, graph=None):
        self._graph = graph if graph else Graph()

    def execute(self, raw_edge):
        edge = tuple([int(n) for n in raw_edge.split(' ')])
        self._graph.add_edge(edge)


class GraphPropsCommand():
    def __init__(self, graph=None):
        self._graph = graph if graph else Graph()

    def execute(self, props):
        matches = re.match(r'\d+\s\d+', props)
        if not matches:
            raise ValueError('Invalid values for graph nodes, edges')
        nodes, edges = tuple([int(p) for p in props.split(' ')])
        self._graph.set_vertices(nodes)
        self._graph.set_edges(edges)


class GraphAdjListDecorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        for vertex, connected_vertices in enumerate(self.f(*args)):
            print(
                f'{vertex}->{"->".join([str(v) for v in connected_vertices])}')


@GraphAdjListDecorator
def show_output(graph):
    return graph.get_adj_list()


def read_input():
    graph = Graph()
    graph_props_command = GraphPropsCommand(graph)
    add_edge_command = GraphAddEdgeCommand(graph)

    try:
        graph_props = input()
        graph_props_command.execute(graph_props)

        user_input = None
        while user_input != '':
            user_input = input()
            if user_input:
                add_edge_command.execute(user_input)

        show_output(graph)
    except Exception as e:
        print(f'{e}')


if __name__ == '__main__':
    read_input()
