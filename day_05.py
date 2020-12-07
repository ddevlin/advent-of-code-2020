from dataclasses import dataclass
from functools import cached_property
from typing import Optional, Sequence, Tuple


def binary_partition(labels: Sequence[str], left_label: str) -> int:
    lower_bound, upper_bound = 0, (2 ** len(labels)) - 1
    for label in labels:
        pivot = lower_bound + ((upper_bound - lower_bound) // 2)
        if label == left_label:
            upper_bound = pivot
        else:
            lower_bound = pivot + 1
    return lower_bound


@dataclass
class Ticket:
    code: str

    @cached_property
    def row(self):
        return binary_partition(self.code[:7], left_label="F")

    @cached_property
    def column(self):
        return binary_partition(self.code[7:], left_label="L")

    @cached_property
    def seat_id(self):
        return (self.row * 8) + self.column


def part_1(tickets: Sequence[Ticket]) -> int:
    return max(ticket.seat_id for ticket in tickets)


def part_2(tickets: Sequence[Ticket]) -> Optional[int]:
    previous_ticket = None
    for ticket in sorted(tickets, key=lambda t: t.seat_id):
        if previous_ticket:
            expected_seat_id = previous_ticket.seat_id + 1
            if expected_seat_id != ticket.seat_id:
                return expected_seat_id
        previous_ticket = ticket
    return None


def preprocess_input(input_: str) -> Tuple[Ticket, ...]:
    return tuple(Ticket(line) for line in input_.splitlines() if line)


def test_solution():
    with open("inputs/day_05.example.txt") as f:
        tickets = preprocess_input(f.read())
    assert tickets[0].row == 70
    assert tickets[0].column == 7
    assert tickets[0].seat_id == 567
    assert part_1(tickets) == 820


if __name__ == "__main__":
    with open("inputs/day_05.txt") as f:
        tickets = preprocess_input(f.read())
    print(f"Part 1: {part_1(tickets)}")
    print(f"Part 2: {part_2(tickets)}")
