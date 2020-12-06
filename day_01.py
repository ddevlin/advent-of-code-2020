from itertools import combinations
from math import prod
from typing import List


def solution(inputs: List[int], n: int) -> int:
    return next(prod(items) for items in combinations(inputs, n) if sum(items) == 2020)


def preprocess_input(input_: str) -> List[int]:
    return [int(s) for s in input_.splitlines() if s]


def test_solution():
    inputs = preprocess_input("1721\n979\n366\n299\n675\n1456\n")
    assert solution(inputs, n=2) == 514579
    assert solution(inputs, n=3) == 241861950


if __name__ == "__main__":
    with open("inputs/day_01.txt") as f:
        inputs = preprocess_input(f.read())
    print(f"Part 1: {solution(inputs, n=2)}")
    print(f"Part 2: {solution(inputs, n=3)}")
