from sgftree import Property, Node, GameTree, Cursor
from sgftree.constants import APP_NAME, APP_VERSION, HANDICAP_SGF_COORDINATES


def make_root_node(width, height, handicap: int = 0, komi: float = 6.5):
    size = f"{width}:{height}" if width != height else width
    root_properties = [
        Property("FF", ["4"]),
        Property("GM", ["1"]),
        Property("AP", [f"{APP_NAME}:{APP_VERSION}"]),
        Property("CA", ["UTF-8"]),
        Property("SZ", [size]),
        Property("HA", [handicap]),
        Property("KM", [komi]),
    ]

    if handicap:
        root_properties.append(Property("AB", HANDICAP_SGF_COORDINATES[handicap]))

    return Node(root_properties)


def make_new_sgf_cursor(width: int, height: int, handicap: int = 0, komi: float = 6.5) -> Cursor:
    root_node = make_root_node(width, height, handicap, komi)
    game_tree = GameTree([root_node])
    return Cursor(game_tree)
