import re
from typing import List
from sgftree.sgflib import Property, Node, GameTree
from sgftree.exceptions import GameTreeParseError, EndOfDataParseError, NodeParseError, PropertyParseError

reGameTreeStart = re.compile(r"\s*\(")
reGameTreeEnd = re.compile(r"\s*\)")
reGameTreeNext = re.compile(r"\s*([;()])")
reNodeContents = re.compile(r"\s*([A-Za-z]+(?=\s*\[))")
rePropertyStart = re.compile(r"\s*\[")
rePropertyEnd = re.compile(r"\]")
reEscape = re.compile(r"\\")
reLineBreak = re.compile(r"\r\n?|\n\r?")  # CR, LF, CR/LF, LF/CR


def convert_control_chars(text):
    """Converts control characters in [text] to spaces. Override for variant behaviour."""
    return text.translate(
        str.maketrans(
            "\000\001\002\003\004\005\006\007\010\011\013\014\016\017\020"
            "\021\022\023\024\025\026\027\030\031\032\033\034\035\036\037",
            " " * 30,
        )
    )


def clean_game_tree(game_tree: GameTree) -> GameTree:
    move_prop = game_tree[0].move_prop
    if move_prop:
        new_node = Node([move_prop])
        game_tree[0].pop_prop(move_prop.label)
        game_tree.data.insert(1, new_node)

    return game_tree


class SGFParser:
    """
    Parser for SGF data. Creates a tree structure based on the SGF standard itself.
    [SGFParser.parse()] will return a [Collection] object for the entire data.
    Instance attributes:
      - self.data : string -- the complete SGF data instance.
      - self.data_len : integer -- length of [self.data].
      - self.index : integer -- current parsing position in [self.data]."""

    def __init__(self, data: str):
        self.data = data
        self.data_len = len(data)
        self.index = 0

    def _match_regex(self, regex):
        return regex.match(self.data, self.index)

    def _search_regex(self, regex):
        return regex.search(self.data, self.index)

    def parse(self) -> List[GameTree]:
        """Parses SGF file contents"""

        game_trees = []
        while self.index < self.data_len:
            sgf_game = self.parse_one_game()

            if not sgf_game:
                break

            game_trees.append(sgf_game)

        return game_trees

    def parse_one_game(self) -> GameTree:
        """Starts parsing game tree when `(` encountered."""

        if self.index < self.data_len:
            match = self._match_regex(reGameTreeStart)
            if match:
                self.index = match.end()
                return clean_game_tree(self.parse_game_tree())

    def parse_game_tree(self) -> GameTree:
        """Parses game tree between matching `(` and `)`."""

        game_tree = GameTree()
        while self.index < self.data_len:
            match = self._match_regex(reGameTreeNext)
            if match:
                self.index = match.end()
                if match.group(1) == ";":  # Start of a node
                    if game_tree.variations:
                        raise GameTreeParseError("A node was encountered after a variation.")
                    game_tree.append(self.parse_node())
                elif match.group(1) == "(":  # Start of variation
                    game_tree.variations = self.parse_variations()
                else:  # End of GameTree ")"
                    return game_tree
            else:
                raise GameTreeParseError("Invalid SGF file format.")
        return game_tree

    def parse_variations(self) -> List[GameTree]:
        """Parses variations of the game tree between `(` and non-matching `)`."""

        variations = []
        while self.index < self.data_len:
            match = self._match_regex(reGameTreeEnd)  # check for the `)` at end of game tree, do not consume it
            if match:
                return variations
            game_tree = self.parse_game_tree()
            if game_tree:
                variations.append(game_tree)
            match = self._match_regex(reGameTreeStart)  # check for next variation, consume `(`
            if match:
                self.index = match.end()

        raise EndOfDataParseError()

    def parse_node(self) -> Node:
        """Parses node after consuming `;`."""

        node = Node()
        while self.index < self.data_len:
            match = self._match_regex(reNodeContents)
            if match:
                self.index = match.end()
                pv_list = self.parse_property_value()
                if pv_list:
                    prop = Property(match.group(1), pv_list)
                    node.add_prop(prop)
                else:
                    raise NodeParseError
            else:  # End of Node
                return node
        raise EndOfDataParseError

    def parse_property_value(self) -> List[str]:
        """Parses property values between `[` and the start of next property, node or variation."""

        pv_list = []
        while self.index < self.data_len:
            match = self._match_regex(rePropertyStart)
            if match:
                self.index = match.end()
                value = ""
                match_end = self._search_regex(rePropertyEnd)
                match_escape = self._search_regex(reEscape)

                # unescape escaped characters (remove linebreaks)
                while match_escape and match_end and (match_escape.end() < match_end.end()):
                    # copy everything up to '\', remove '\'
                    value += self.data[self.index : match_escape.start()]
                    match_break = reLineBreak.match(self.data, match_escape.end())
                    if match_break:
                        # skip linebreak
                        self.index = match_break.end()
                    else:
                        # copy escaped character and move to point after it
                        value += self.data[match_escape.end()]
                        self.index = match_escape.end() + 1
                    match_end = self._search_regex(rePropertyEnd)
                    match_escape = self._search_regex(reEscape)
                if match_end:
                    value += self.data[self.index : match_end.start()]
                    self.index = match_end.end()
                    pv_list.append(convert_control_chars(value))
                else:
                    raise PropertyParseError
            else:  # end of property
                break

        # property cannot be empty
        if len(pv_list):
            return pv_list
        else:
            raise PropertyParseError
