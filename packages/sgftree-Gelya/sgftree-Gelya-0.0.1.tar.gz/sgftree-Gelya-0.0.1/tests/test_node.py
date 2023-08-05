import pytest

from sgftree import Property, Node


prop_b = Property("B", ["aa"])
prop_w = Property("W", ["ab"])
prop_c = Property("C", ["comment"])
prop_many1 = Property("TR", ["v1", "v2"])
prop_many2 = Property("TR", ["v3", "v4"])


@pytest.mark.parametrize(
    "props, expected", [([], ";"), ([prop_b], ";B[aa]"), ([prop_b, prop_many1], ";B[aa]TR[v1][v2]"), ]
)
def test_node_create(props, expected):
    node = Node(props)

    assert str(node) == expected


@pytest.mark.parametrize(
    "node1, node2, expected",
    [
        (Node([]), Node([]), ";"),
        (Node([prop_b]), Node([prop_b, prop_c]), ";B[aa]C[comment]"),
        (Node([prop_b]), Node([prop_b, prop_many1]), ";B[aa]TR[v1][v2]"),
        (Node([prop_b, prop_many1]), Node([prop_b, prop_many2]), ";B[aa]TR[v1][v2][v3][v4]"),
    ],
)
def test_node_merge(node1, node2, expected):
    node1.merge(node2)

    assert str(node1) == expected
