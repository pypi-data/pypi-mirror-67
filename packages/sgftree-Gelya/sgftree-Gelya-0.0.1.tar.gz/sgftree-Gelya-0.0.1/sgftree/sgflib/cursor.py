import re

from sgftree.sgflib import Node, GameTree
from sgftree.exceptions import GameTreeNavigationError, GameTreeEndError

reCharsToEscape = re.compile(r"[]\\]")  # characters that need to be \escaped


class Cursor:
    """
    [GameTree] navigation tool. Instance attributes:
      - self.game : [GameTree] -- The root [GameTree].
      - self.game_tree : [GameTree] -- The current [GameTree].
      - self.node : [Node] -- The current Node.
      - self.node_num : integer -- The offset of [self.node] from the root of [self.game].
        The node_num of the root node is 0.
      - self.index : integer -- The offset of [self.node] within [self.game_tree].
      - self.stack : list of [GameTree] -- A record of [GameTree]s traversed.
      - self.children : list of [Node] -- All child nodes of the current node.
      - self.atEnd : boolean -- Flags if we are at the end of a branch.
      - self.atStart : boolean -- Flags if we are at the start of the game."""

    def __init__(self, game_tree: GameTree):
        self.game_tree = self.game = game_tree
        self.index = 0
        self.stack = []
        self.path = []
        self._set_flags()

    @property
    def root_node(self):
        return self.game[0]

    @property
    def node(self) -> Node:
        return self.game_tree[self.index]

    @property
    def move_number(self):
        return len(self.path)

    def reset(self):
        """Set 'Cursor' to point to the start of the root 'GameTree', 'self.game'."""
        self.__init__(self.game)

    def next(self, variation: int = 0):
        """
        Moves the [Cursor] to the next [Node] and returns it.
        Raises [GameTreeEndError] if the end of a branch is exceeded.
        Raises [GameTreeNavigationError] if a non-existent variation is accessed.
        Argument:
        - variation : integer, default 0 -- Variation number.
          Non-zero only valid at a branching, where variations exist."""
        if self.index + 1 < len(self.game_tree):  # more main line?
            if variation != 0:
                raise GameTreeNavigationError
            self.index += 1
        elif self.game_tree.variations:  # variations exist?

            if variation < len(self.game_tree.variations):
                self.stack.append(self.game_tree)
                self.game_tree = self.game_tree.variations[variation]
                self.index = 0
            else:
                raise GameTreeNavigationError
        else:
            raise GameTreeEndError

        self.path.append(variation)
        self._set_flags()

        return self.node

    def previous(self):
        """
        Moves the [Cursor] to the previous [Node] and returns it.
        Raises [GameTreeEndError] if the start of a branch is exceeded."""
        if self.index > 0:  # more main line?
            self.index -= 1
        elif self.stack:  # were we in a variation?
            self.game_tree = self.stack.pop()
            self.index = len(self.game_tree) - 1
        else:
            raise GameTreeEndError

        self.path.pop()
        self._set_flags()

        return self.node

    def jump_to(self, path: list):
        """Goes to specified position"""
        self.reset()

        for variation in path:
            self.next(variation)

        return self.node

    def append_node(self, node: Node):
        self.game_tree.insert_tree(self.index + 1, GameTree([node]))
        self._set_flags()

    def _set_flags(self):
        """Sets up the flags [self.atEnd] and [self.atStart]."""
        self.atStart = not self.stack and (self.index == 0)
        self.atSplit = (self.index + 1 == len(self.game_tree)) and bool(self.game_tree.variations)
        self.atEnd = (self.index + 1 == len(self.game_tree)) and not self.game_tree.variations
