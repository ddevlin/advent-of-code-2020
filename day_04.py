from dataclasses import dataclass, field
from re import compile
from typing import Optional, Sequence, Tuple


@dataclass
class Passport:
    byr: Optional[str] = None
    iyr: Optional[str] = None
    eyr: Optional[str] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
    cid: Optional[str] = None

    required_fields: Tuple[str, ...] = field(
        init=False, default=("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    )

    def valid_byr(self) -> bool:
        return (
            self.byr is not None
            and self.byr.isnumeric()
            and 1920 <= int(self.byr) <= 2002
        )

    def valid_iyr(self) -> bool:
        return (
            self.iyr is not None
            and self.iyr.isnumeric()
            and 2010 <= int(self.iyr) <= 2020
        )

    def valid_eyr(self) -> bool:
        return (
            self.eyr is not None
            and self.eyr.isnumeric()
            and 2020 <= int(self.eyr) <= 2030
        )

    def valid_hgt(self) -> bool:
        pattern = compile(r"^(\d*)(in|cm)$")
        if match := pattern.match(self.hgt or ""):
            num, unit = int(match[1]), match[2]
            if unit == "cm":
                return 150 <= num <= 193
            if unit == "in":
                return 59 <= num <= 76
        return False

    def valid_hcl(self) -> bool:
        pattern = compile(r"^#([0-9a-f]){6}$")
        return bool(pattern.match(self.hcl or ""))

    def valid_ecl(self) -> bool:
        return self.ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def valid_pid(self) -> bool:
        return (self.pid or "").isnumeric() and len(self.pid or "") == 9

    @property
    def is_valid_part_1(self) -> bool:
        return all(getattr(self, field, None) for field in self.required_fields)

    @property
    def is_valid_part_2(self) -> bool:
        return all(getattr(self, f"valid_{field}")() for field in self.required_fields)


def part_1(passports: Sequence[Passport]) -> int:
    return len(tuple(passport for passport in passports if passport.is_valid_part_1))


def part_2(passports: Sequence[Passport]) -> int:
    return len(tuple(passport for passport in passports if passport.is_valid_part_2))


def preprocess_input(input_: str) -> Tuple[Passport, ...]:
    return tuple(
        Passport(
            **{
                str(k): v
                for k, v in (item.split(":", maxsplit=1) for item in lines.split())
            }
        )
        for lines in input_.split("\n\n")
        if lines
    )


def test_solution():
    with open("inputs/day_04.example.txt") as f:
        passports = preprocess_input(f.read())
    assert part_1(passports) == 2

    with open("inputs/day_04.example.invalid.txt") as f:
        passports = preprocess_input(f.read())
    assert part_2(passports) == 0

    with open("inputs/day_04.example.valid.txt") as f:
        passports = preprocess_input(f.read())
    assert part_2(passports) == 4


if __name__ == "__main__":
    with open("inputs/day_04.txt") as f:
        rows = preprocess_input(f.read())
    print(f"Part 1: {part_1(rows)}")
    print(f"Part 2: {part_2(rows)}")
