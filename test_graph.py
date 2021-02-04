from graph import Graph


def test_create_graph():
    g = Graph()
    assert isinstance(g, Graph) == True


def test_nodes():
    g = Graph()
    g.set_vertices(5)
    assert g.vertices == 5


def test_edges():
    g = Graph()
    g.set_edges(7)
    assert g.edges == 7


def test_add_edge():
    g = Graph(nodes=5,edges=7)
    g.add_edge((0,1))

    assert g.get_adj_list() == [
        [1],
        [0],
        [],
        [],
        []
    ]


def test_get_adj_list_multiple_edges():
    g = Graph(nodes=5,edges=7)
    g.add_edge((0,1))
    g.add_edge((0,4))
    g.add_edge((1,2))

    assert g.get_adj_list() == [
        [1, 4],
        [0, 2],
        [1],
        [],
        [0]
    ]


def test_get_adj_list_all_edges():
    g = Graph(nodes=5,edges=7)
    g.add_edge((0,1))
    g.add_edge((0,4))
    g.add_edge((1,2))
    g.add_edge((1,3))
    g.add_edge((1,4))
    g.add_edge((2,3))
    g.add_edge((3,4))

    assert g.get_adj_list() == [
        [1, 4],
        [0, 2, 3, 4],
        [1, 3],
        [1, 2, 4],
        [0, 1, 3]
    ]


def test_get_adj_list_add_edge_same_vertex():
    g = Graph(nodes=5,edges=7)
    g.add_edge((3,3))

    assert g.get_adj_list() == [
        [],
        [],
        [],
        [],
        []
    ]

def test_add_more_than_limit_edge_list():
    g = Graph(nodes=5,edges=7)
    g.add_edge((0,1))
    g.add_edge((0,4))
    g.add_edge((1,2))
    g.add_edge((1,3))
    g.add_edge((1,4))
    g.add_edge((2,3))
    g.add_edge((3,4))
    g.add_edge((0,1))

    assert g.get_adj_list() == [
        [1, 4],
        [0, 2, 3, 4],
        [1, 3],
        [1, 2, 4],
        [0, 1, 3]
    ]


