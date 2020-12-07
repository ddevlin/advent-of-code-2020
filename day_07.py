import re
from typing import Dict


Rules = Dict[str, Dict[str, int]]


def contains(rules: Rules, parent: str, child: str):
    return any(
        candidate == child or contains(rules, candidate, child)
        for candidate in rules.get(parent, {})
    )


def contains_count(rules: Rules, parent: str):
    return 1 + sum(
        contains_count(rules, child) * count
        for child, count in rules.get(parent, {}).items()
    )


def part_1(rules: Rules) -> int:
    return sum(1 for bag in rules if contains(rules, bag, "shiny gold"))


def part_2(rules: Rules) -> int:
    return contains_count(rules, "shiny gold") - 1  # subtract 1 for the shiny gold bag itself


def preprocess_input(input_: str) -> Rules:
    rules: Rules = {}
    pattern = re.compile(r"(\d+)? ?(\w+ \w+) bags?")
    for line in input_.splitlines():
        if matches := pattern.findall(line):
            (_, bag), *children = matches
            rules[bag] = {child_bag: int(num) for num, child_bag in children if num}
    return rules


def test_solution():
    with open("inputs/day_07.example.txt") as f:
        rules = preprocess_input(f.read())
    assert part_1(rules) == 4
    assert part_2(rules) == 32

    with open("inputs/day_07.other_example.txt") as f:
        rules = preprocess_input(f.read())
    assert part_2(rules) == 126


if __name__ == "__main__":
    with open("inputs/day_07.txt") as f:
        rules = preprocess_input(f.read())
    print(f"Part 1: {part_1(rules)}")
    print(f"Part 2: {part_2(rules)}")
