import pytest

from sgftree import Property, Node, GameTree


prop_move1 = Property("B", ["aa"])
prop_move2 = Property("W", ["ab"])
prop_move3 = Property("B", ["ac"])
prop_move4 = Property("W", ["ad"])
prop_move5 = Property("B", ["ae"])
prop_many1 = Property("TR", ["v1", "v2"])
prop_many2 = Property("TR", ["v3", "v4"])

node1 = Node([prop_move1])
node2 = Node([prop_move2])
node3 = Node([prop_move3])
node4 = Node([prop_move4])
node5 = Node([prop_move5])

node6 = Node([prop_move3, prop_many1])
node7 = Node([prop_move3, prop_many2])


@pytest.mark.parametrize(
    "nodes, variations, expected",
    [
        ([node1], [], "(;B[aa])"),
        ([node1, node2, node3], [], "(;B[aa]\n;W[ab]\n;B[ac])"),
        ([node1], [GameTree([node2]), GameTree([node4])], "(;B[aa]\n(;W[ab])\n(;W[ad]))"),
        ([node1], [GameTree([node2])], "(;B[aa]\n;W[ab])"),
    ],
)
def test_game_tree_create(nodes, variations, expected):
    node = GameTree(nodes, variations)

    assert str(node) == expected


@pytest.mark.parametrize(
    "tree1, tree2, index, expected",
    [
        (GameTree([node1, node2, node3]), GameTree([node4, node3]), 1, "(;B[aa]\n(;W[ab]\n;B[ac])\n(;W[ad]\n;B[ac]))"),
        (GameTree([node1, node2, node3]), GameTree([node5, node4]), 2, "(;B[aa]\n;W[ab]\n(;B[ac])\n(;B[ae]\n;W[ad]))"),
        (GameTree([node1, node2, node3]), GameTree([node4, node5]), 3, "(;B[aa]\n;W[ab]\n;B[ac]\n;W[ad]\n;B[ae])"),
        (GameTree([node1, node2, node3]), GameTree([node1, node2, node3]), 0, "(;B[aa]\n;W[ab]\n;B[ac])"),
        (GameTree([node1, node2]), GameTree([node1, node2, node3, node4]), 0, "(;B[aa]\n;W[ab]\n;B[ac]\n;W[ad])"),
        (
            GameTree([node1, node2], [GameTree([node3, node4]), GameTree([node5, node4])]),
            GameTree([node1, node2, node3, node4]),
            0,
            "(;B[aa]\n;W[ab]\n(;B[ac]\n;W[ad])\n(;B[ae]\n;W[ad]))",
        ),
        (
            GameTree([node1, node2], [GameTree([node6, node4]), GameTree([node5, node4])]),
            GameTree(
                [node1, node2], [GameTree([node7, node4]), GameTree([node5], [GameTree([node4]), GameTree([node2])])]
            ),
            0,
            "(;B[aa]\n;W[ab]\n(;B[ac]TR[v1][v2][v3][v4]\n;W[ad])\n(;B[ae]\n(;W[ad])\n(;W[ab])))",
        ),
    ],
)
def test_game_tree_merge(tree1, tree2, index, expected):
    tree = tree1.merge(tree2, index)
    print(str(tree))
    x = str(tree)
    assert x == expected
