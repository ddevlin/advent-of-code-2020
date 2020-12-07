from dataclasses import dataclass
from typing import Sequence, Tuple


@dataclass
class Group:
    input_lines: str

    @property
    def questions_anyone_answered(self) -> int:
        return len({char for char in self.input_lines.replace("\n", "") if char})

    @property
    def questions_everyone_answered(self) -> int:
        return len(
            set.intersection(*(set(line) for line in self.input_lines.splitlines()))
        )


def part_1(groups: Sequence[Group]) -> int:
    return sum(group.questions_anyone_answered for group in groups)


def part_2(groups: Sequence[Group]) -> int:
    return sum(group.questions_everyone_answered for group in groups)


def preprocess_input(input_: str) -> Tuple[Group, ...]:
    return tuple(Group(lines) for lines in input_.split("\n\n") if lines)


def test_solution():
    with open("inputs/day_06.example.txt") as f:
        groups = preprocess_input(f.read())
    assert part_1(groups) == 11
    assert part_2(groups) == 6


if __name__ == "__main__":
    with open("inputs/day_06.txt") as f:
        groups = preprocess_input(f.read())
    print(f"Part 1: {part_1(groups)}")
    print(f"Part 2: {part_2(groups)}")
