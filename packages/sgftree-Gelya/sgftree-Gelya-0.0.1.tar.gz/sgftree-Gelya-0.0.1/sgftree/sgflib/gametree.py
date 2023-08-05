from typing import List

from sgftree.sgflib import Property, Node
from sgftree.exceptions import GameTreeIndexError


class GameTree:
    """
    An SGF game tree.

    Example:
        (;SZ[19]KM[6.5]RU[Japanese];B[dc]
            (;W[qp]C[White played komoku];B[dp])
            (;W[pp]C[White played hoshi]))

    """

    def __init__(self, nodes: List[Node] = None, variations: List["GameTree"] = None):
        self.data = nodes or []

        variations = variations or []
        if len(variations) == 1:
            self.data.extend(variations[0].data)
            self.variations = variations[0].variations
        else:
            self.variations = variations

    def __str__(self):
        """SGF representation of game tree, with line breaks between nodes."""
        if self.data:
            return "(" + "\n".join([str(x) for x in self.data + self.variations]) + ")"
        else:
            return ""

    def __getitem__(self, item: int):
        return self.data[item]

    def __setitem__(self, key: int, value: "Node"):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

    def copy(self):
        return GameTree([node.copy() for node in self.data], [tree.copy() for tree in self.variations])

    def append(self, node: Node):
        self.data.append(node)

    def rotate(self, flip_x: bool, flip_y: bool, swap_xy: bool) -> "GameTree":
        return GameTree([node.rotate(flip_x, flip_y, swap_xy) for node in self.data],
                        [tree.rotate(flip_x, flip_y, swap_xy) for tree in self.variations])

    def mainline(self) -> "GameTree":
        """Returns the main line of the game (variation A) as a [GameTree]."""
        if self.variations:
            return GameTree(self.data + self.variations[0].mainline().data)
        else:
            return self

    def get_subtree(self, start: int, end: int = None):
        if start >= len(self):
            raise GameTreeIndexError("Tree should have at least one node")

        if end is None:
            return GameTree(self.data[start:], [tree.copy() for tree in self.variations])

        if end <= len(self):
            return GameTree(self.data[start:end])

        return GameTree(self.data[start:], [tree.get_subtree(0, end - len(self)) for tree in self.variations])

    @property
    def first_move_prop(self):
        return self[0].move_prop

    @property
    def variation_move_props(self) -> List[Property]:
        return [variation[0].move_prop for variation in self.variations]

    def move_variation(self, move_prop: Property) -> int:
        if move_prop in self.variation_move_props:
            return self.variation_move_props.index(move_prop)

    def replace_variation(self, index: int, new_tree: "GameTree"):
        self.variations[index] = new_tree

    def remove_variation(self, index: int):
        self.variations.pop(index)

        if len(self.variations) == 1:
            self.data.extend(self.variations[0].data)
            self.variations = self.variations[0].variations

    def insert_tree(self, index: int, new_tree: "GameTree"):
        if index == 0:
            raise GameTreeIndexError("Cannot insert tree to first node")
        if index < len(self):
            self.data, existing_tree = self.data[:index], self.get_subtree(index)
            self.variations = [existing_tree, new_tree]
        elif self.variations:
            self.variations.append(new_tree)
        else:
            self.data.extend(new_tree.data)
            self.variations = new_tree.variations

        return self

    def remove_tree(self, index: int):
        if index >= len(self):
            raise IndexError
        self.data = self.data[:index]
        self.variations = []

    def merge(self, new_tree: "GameTree", index: int = 0):
        # go over moves and merge nodes with the same move
        tree_index = 0
        while index < len(self) and tree_index < len(new_tree):

            merged_node = self[index]
            tree_node = new_tree[tree_index]

            if merged_node.move_prop != tree_node.move_prop:
                return self.insert_tree(index, new_tree.get_subtree(tree_index))

            # merge node data if move is the same
            merged_node.merge(tree_node)

            index += 1
            tree_index += 1

        # both trees have ended, merge matching variations, insert others
        if index == len(self) and tree_index == len(new_tree):
            for new_subtree in new_tree.variations:
                existing_idx = self.move_variation(new_subtree.first_move_prop)

                if existing_idx is not None:
                    self.variations[existing_idx].merge(new_subtree)
                    # self.replace_variation(existing_idx, new_variation)
                else:
                    self.insert_tree(index, new_subtree)

        # merged tree ended, merge rest of subtree with a matching variation, insert otherwise
        elif index == len(self):
            tree_move = new_tree[tree_index].move_prop
            existing_idx = self.move_variation(tree_move)

            if existing_idx is not None:
                self.variations[existing_idx].merge(new_tree.get_subtree(tree_index))
            else:
                self.insert_tree(index, new_tree.get_subtree(tree_index))

        # new tree ended, merge variations
        else:
            for subtree in new_tree.variations:
                self.merge(subtree, index)

        return self
