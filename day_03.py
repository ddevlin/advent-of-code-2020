from dataclasses import dataclass
from math import prod
from typing import Sequence, Tuple


@dataclass
class Row:
    trees: str

    def is_tree(self, i):
        return self.trees[i % len(self.trees)] == "#"


def part_1(rows: Sequence[Row], right: int = 3, down: int = 1) -> int:
    return sum(1 for i, row in enumerate(rows[0::down]) if row.is_tree(i * right))


def part_2(rows: Sequence[Row]) -> int:
    return prod(
        part_1(rows, right, down)
        for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    )


def preprocess_input(input_: str) -> Tuple[Row, ...]:
    return tuple(Row(line) for line in input_.splitlines() if line)


def test_solution():
    with open("inputs/day_03.example.txt") as f:
        rows = preprocess_input(f.read())
    assert part_1(rows) == 7
    assert part_2(rows) == 336


if __name__ == "__main__":
    with open("inputs/day_03.txt") as f:
        rows = preprocess_input(f.read())
    print(f"Part 1: {part_1(rows)}")
    print(f"Part 2: {part_2(rows)}")
