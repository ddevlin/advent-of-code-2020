from dataclasses import dataclass
from enum import Enum
from typing import Dict, Set, Tuple


class Operation(Enum):
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"


@dataclass
class Instruction:
    op: Operation
    arg: int


Instructions = Dict[int, Instruction]


def cpu(instructions: Instructions) -> Tuple[int, bool]:
    accumulator, counter = 0, 0
    visited: Set[int] = set()

    while instruction := instructions.get(counter):
        if counter in visited:
            break
        visited.add(counter)
        counter += instruction.arg if instruction.op is Operation.JMP else 1

        if instruction.op is Operation.ACC:
            accumulator += instruction.arg

    terminated = instruction is None
    return accumulator, terminated


def part_1(instructions: Instructions) -> int:
    accumulator, _ = cpu(instructions)
    return accumulator


def part_2(instructions: Instructions) -> int:
    accumulator = 0
    for i, instruction in instructions.items():
        if instruction.op is Operation.ACC:
            continue
        if instruction.op is Operation.NOP:
            new_instruction = Instruction(Operation.JMP, instruction.arg)
        else:
            new_instruction = Instruction(Operation.NOP, instruction.arg)

        accumulator, terminated = cpu({**instructions, i: new_instruction})
        if terminated:
            break
    return accumulator


def preprocess_input(input_: str) -> Instructions:
    return {
        i: Instruction(Operation(operation), int(argument))
        for i, (operation, argument) in enumerate(
            line.split(" ") for line in input_.splitlines() if line
        )
    }


def test_solution():
    with open("inputs/day_08.example.txt") as f:
        instructions = preprocess_input(f.read())
    assert part_1(instructions) == 5
    assert part_2(instructions) == 8


if __name__ == "__main__":
    with open("inputs/day_08.txt") as f:
        instructions = preprocess_input(f.read())
    print(f"Part 1: {part_1(instructions)}")
    print(f"Part 2: {part_2(instructions)}")
