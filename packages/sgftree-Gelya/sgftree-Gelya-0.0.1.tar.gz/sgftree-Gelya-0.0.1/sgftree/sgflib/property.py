from sgftree.exceptions import PropertyMergeError
from sgftree.utils import escape_text

COORDINATES = dict(zip('abcdefghijklmnopqrs', 'srqponmlkjihgfedcba'))


class Property:
    """
    An SGF property.

    Examples:
        B[dd] - black move at [dd]
        W[qq] - white move at [qq]
        C[this is comment] - comment
        LB[aa:A][bb:B] - labels: `A` at [aa] and `B` at [bb]
    """

    def __init__(self, label: str, prop_values: list):
        self.data = sorted(set([escape_text(str(value)) for value in prop_values if value]))
        self.label = label

    def __str__(self):
        if not self.data:
            return ""

        if self.label == "C":
            # concatenate comments
            return self.label + "[" + "\n----------\n".join(self.data) + "]"

        return self.label + "[" + "][".join(self.data) + "]"

    def __hash__(self):
        return hash(str(self))

    def __getitem__(self, item: int) -> str:
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __eq__(self, other: "Property"):
        return other is not None and self.label == other.label and self.data == other.data

    def copy(self) -> "Property":
        return Property(self.label, self.data.copy())

    def merge(self, prop: "Property") -> "Property":
        """
        Adds values from another property
        """
        if self.label != prop.label:
            raise PropertyMergeError(f"labels not equal: {self.label} != {prop.label}")

        # check there is only one move in the property
        if self.label in ["B", "W"] and len(set(self.data) | set(prop.data)) > 1:
            raise PropertyMergeError(f"multiple moves: {set(self.data) | set(prop.data)}")

        self.data = sorted(set(self.data) | set(prop.data))

        return self

    @staticmethod
    def _rotate_coord(xy: str, flip_x: bool, flip_y: bool, swap_xy: bool) -> str:
        if len(xy) != 2 or xy == "tt":
            return xy

        x = COORDINATES[xy[0]] if flip_x else xy[0]
        y = COORDINATES[xy[1]] if flip_y else xy[1]

        return y + x if swap_xy else x + y

    def rotate(self, flip_x: bool, flip_y: bool, swap_xy: bool) -> "Property":

        if self.label in ["B", "W", "AB", "AW", "AE", "CR", "DD", "MA", "SL", "SQ", "TR", "TB", "TW"]:
            new_values = [self._rotate_coord(xy, flip_x, flip_y, swap_xy) for xy in self.data]

        elif self.label in ["AR", "LN"]:
            new_values = []
            for item in self.data:
                xy1, xy2 = item.split(":", maxsplit=1)
                xy1 = self._rotate_coord(xy1, flip_x, flip_y, swap_xy)
                xy2 = self._rotate_coord(xy2, flip_x, flip_y, swap_xy)
                new_values.append(f"{xy1}:{xy2}")

        elif self.label == "LB":
            new_values = []
            for item in self.data:
                xy, comment = item.split(":", maxsplit=1)
                xy = self._rotate_coord(xy, flip_x, flip_y, swap_xy)
                new_values.append(f"{xy}:{comment}")
        else:
            return self.copy()

        return Property(self.label, new_values)
