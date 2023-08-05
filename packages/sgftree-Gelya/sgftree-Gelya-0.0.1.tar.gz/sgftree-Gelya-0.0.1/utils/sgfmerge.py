import os
import time
import argparse
from typing import List
from sgftree import SGFParser, GameTree, Node, Property


def parse_sgf_file(sgf_path: str) -> GameTree:
    with open(sgf_path) as f:
        sgf_data = f.read()

    sgf_parser = SGFParser(sgf_data)
    sgf = sgf_parser.parse()

    return sgf[0]


def collect_trunks(game_tree: GameTree) -> List[List[Node]]:
    if not game_tree.variations:
        return [game_tree.data, ]

    trees = []
    common_data = game_tree.data
    for variation in game_tree.variations:
        nested_trees = collect_trunks(variation)

        for nt in nested_trees:
            trees.append(common_data + nt)

    return trees


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source_path", type=str, help="Path to directory with *.sgf files to merge")
    parser.add_argument("-o", "--output", dest="target_path", default="merged.sgf", help="Path to save merged file")
    parser.add_argument("-l", "--length", dest="tree_length", default=50, help="How many moves to save")
    parser.add_argument("-r", "--rotate", action="store_true", help="Add rotated and flipped variations")

    args = parser.parse_args()

    time_start = time.time()
    sgf_list = []
    idx = -1
    print("Collecting data from SGF files...")
    for idx, name in enumerate([path for path in os.listdir(args.source_path) if path.endswith(".sgf")]):
        try:
            sgf_list.append(parse_sgf_file(os.path.join(args.source_path, name)))
            print(".", end="")
        except Exception as ex:
            print(f"F", end="")

        if not (idx + 1) % 100:
            print(f"\nProcessed {idx + 1} games in {time.time() - time_start:.2f} seconds")

    print(f"\nProcesses {idx + 1} games in {time.time() - time_start:.2f} seconds")
    print(f"Successfully loaded games: {len(sgf_list)}")

    merged_sgf = GameTree([Node([Property("C", [f"Total games: {len(sgf_list)}"])])])
    total_trunks = 0

    time_start = time.time()
    for idx, sgf in enumerate(sgf_list):
        if not (idx + 1) % 100:
            print(f"\nProcessed {idx+1} games in {time.time() - time_start:.2f} seconds")
        else:
            print(".", end="")

        merged_sgf.merge(sgf.get_subtree(0, args.tree_length + 1))

    merged_sgf.data[0] = Node([Property("C", [f"Total games: {len(sgf_list)}"])])

    time_end = time.time()
    print(f"\nProcessed {len(sgf_list)} in {time_end - time_start} seconds")
    counted_trunks = collect_trunks(merged_sgf)
    print(f"Total variations: {len(counted_trunks)}")

    with open(args.target_path, mode="w") as sgf_file:
        sgf_file.write(str(merged_sgf))
