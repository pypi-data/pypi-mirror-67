import re
from sgftree.constants import SGF_COORDINATES


class ParserError(Exception):
    pass


reCharsToEscape = re.compile(r"[]\\]")  # characters that need to be \escaped


def escape_text(text: str):
    """Adds backslash-escapes to property value characters that need them."""
    output = ""
    index = 0
    match = reCharsToEscape.search(text, index)

    while match:
        output = output + text[index : match.start()] + "\\" + text[match.start()]
        index = match.end()
        match = reCharsToEscape.search(text, index)

    output += text[index:]
    return output


def swap_substring(s: str, trans: dict) -> str:
    new_values = []
    for item in s.split(" "):
        new_values.append(trans[item] if item in trans else item)

    return " ".join(new_values)


def sgf_coord_to_int(coord: str) -> tuple:
    if len(coord) != 2:
        raise ParserError("Wrong coordinates")

    x = SGF_COORDINATES.index(coord[0])
    y = SGF_COORDINATES.index(coord[1])
    return y, x


def int_coord_to_sgf(coord: tuple) -> str:
    if len(coord) != 2:
        raise ParserError("Wrong coordinates")

    x = SGF_COORDINATES[coord[0]]
    y = SGF_COORDINATES[coord[1]]
    return f"{y}{x}"
