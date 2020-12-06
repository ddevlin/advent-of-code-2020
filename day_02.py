from dataclasses import dataclass
from re import compile
from typing import Sequence, Tuple


@dataclass
class Password:
    arg1: int
    arg2: int
    char: str
    text: str


def part_1(passwords: Sequence[Password]) -> int:
    return len([p for p in passwords if p.arg1 <= p.text.count(p.char) <= p.arg2])


def part_2(passwords: Sequence[Password]) -> int:
    return len(
        tuple(
            p
            for p in passwords
            if (p.text[p.arg1 - 1] == p.char) != (p.text[p.arg2 - 1] == p.char)
        )
    )


def preprocess_input(input_: str) -> Tuple[Password, ...]:
    pattern = compile(r"(\d*)\-(\d*) (\w): (\w*)?")
    return tuple(
        Password(int(match[1]), int(match[2]), match[3], match[4])
        for line in input_.splitlines()
        if (match := pattern.match(line))
    )


def test_solution():
    with open("inputs/day_02.example.txt") as f:
        passwords = preprocess_input(f.read())
    assert part_1(passwords) == 2
    assert part_2(passwords) == 1


if __name__ == "__main__":
    with open("inputs/day_02.txt") as f:
        passwords = preprocess_input(f.read())
    print(f"Part 1: {part_1(passwords)}")
    print(f"Part 2: {part_2(passwords)}")
