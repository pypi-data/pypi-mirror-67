from typing import List

from sgftree.sgflib import Property
from sgftree.exceptions import NodeMergeError, NodePropertyError


class Node:
    """
    An SGF node.

    Examples:
        ;B[dd]C[Black played at 4-4] - node with black move at [dd] and a comment
        ;SZ[19]C[The game starts here]LB[dd:A] - node with board size 19, comment and label `A` at [dd]
    """

    def __init__(self, props: List[Property] = None):
        self.data = {}
        props = props or []
        for prop in props:
            if prop:
                self.add_prop(prop)

    def __str__(self):
        return ";" + "".join([str(prop) for prop in self.data.values()])

    def __getitem__(self, item: str):
        return self.data[item]

    def __setitem__(self, key: str, value: Property):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

    def get(self, label: str) -> Property:
        return self.data.get(label)

    def get_prop_value(self, label: str) -> List[Property]:
        prop = self.get(label)
        return prop.data if prop else []

    def get_values(self, labels: list) -> dict:
        return {label: self.get_prop_value(label) for label in labels}

    def copy(self) -> "Node":
        return Node([prop.copy() for prop in self.data.values()])

    def add_prop(self, prop: Property):
        """
        Adds property to the node.
        The node cannot have both black and white move
        """
        if prop.label in self.data:
            raise NodePropertyError(f"Duplicated property: {prop.label}")

        if prop.label == "B" and "W" in self.data or prop.label == "W" and "B" in self.data:
            raise NodePropertyError(f"Another move: {prop}")

        self[prop.label] = prop

    def pop_prop(self, label: str):
        self.data.pop(label, None)

    def merge(self, node: "Node") -> "Node":
        """
        Merges properties from another node.
        The node cannot have several black or white moves
        """
        if self.move_prop is not None and self.move_prop != node.move_prop:
            raise NodeMergeError(f"Different move properties: {self.move_prop} != {node.move_prop}")

        for prop in node.data.values():
            if prop.label in self.data:
                self[prop.label].merge(prop)
            else:
                self.add_prop(prop)

        return self

    @property
    def move_prop(self) -> Property:
        return self.get("B") or self.get("W")

    @property
    def setup_props(self) -> dict:
        return self.get_values(["AB", "AW", "AE"])

    def rotate(self, flip_x: bool, flip_y: bool, swap_xy: bool) -> "Node":
        return Node([prop.rotate(flip_x, flip_y, swap_xy) for prop in self.data.values()])
