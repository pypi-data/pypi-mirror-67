from sgftree import Property, Node, Board
from sgftree.helpers import make_new_sgf_cursor
from sgftree.utils import sgf_coord_to_int


class SGF:
    def __init__(self, width: int, height: int, handicap: int = 0, komi: float = 7.5):
        self.cursor = make_new_sgf_cursor(width, height, handicap, komi)
        self.board = Board((width, height), handicap=handicap)

    @property
    def turn(self):
        return self.board.turn_color

    def __str__(self):
        return str(self.cursor.game)

    @property
    def turn_label(self):
        return "B" if self.turn == "black" else "W"

    @property
    def time_label(self):
        return "BL" if self.turn == "black" else "WL"

    def is_valid_move(self, coord):
        return bool(self.board.legal_moves[sgf_coord_to_int(coord)])

    def make_move(self, coord: str, time_left: float = 0.0):
        node = Node([
            Property(self.turn_label, [coord]),
            Property(self.time_label, [f"{time_left:.2f}"])
        ])

        self.board.move(sgf_coord_to_int(coord))

        self.cursor.append_node(node)
        self.cursor.next()

    def make_pass(self, time_left: float = 0.0):
        node = Node([
            Property(self.turn_label, []),
            Property(self.time_label, [f"{time_left:.2f}"])
        ])

        self.board.make_pass()

        self.cursor.append_node(node)
        self.cursor.next()

    def undo(self):
        self.board.undo()
        self.cursor.previous()
