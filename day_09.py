from typing import List, Set


def part_1(numbers: List[int], preamble: int) -> int:
    candidate = 0
    valid_numbers: List[Set[int]] = []
    for i, candidate in enumerate(numbers):
        if preamble <= i and candidate not in set.union(*valid_numbers):
            break
        preamble_numbers = numbers[max(0, i - preamble):i]
        valid_numbers.append(
            {candidate + previous for previous in preamble_numbers if candidate != previous}
        )
        valid_numbers = valid_numbers[-preamble:]

    return candidate


def part_2(numbers: List[int], preamble: int) -> int:
    invalid_number = part_1(numbers, preamble)
    sequence = []
    for number in numbers:
        sequence.append(number)

        if len(sequence) < 2:
            continue

        while invalid_number < sum(sequence):
            sequence.pop(0)

        if sum(sequence) == invalid_number:
            break

    return min(sequence) + max(sequence)


def preprocess_input(input_: str) -> List[int]:
    return [int(line) for line in input_.splitlines() if line]


def test_solution():
    with open("inputs/day_09.example.txt") as f:
        numbers = preprocess_input(f.read())
    assert part_1(numbers, preamble=5) == 127
    assert part_2(numbers, preamble=5) == 62


if __name__ == "__main__":
    with open("inputs/day_09.txt") as f:
        numbers = preprocess_input(f.read())
    print(f"Part 1: {part_1(numbers, preamble=25)}")
    print(f"Part 2: {part_2(numbers, preamble=25)}")
