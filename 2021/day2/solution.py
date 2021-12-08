from __future__ import annotations
from typing import List, NamedTuple
from pathlib import Path

from solver import TestCase, log_time, test


class Instruction(NamedTuple):
    move: str
    units: int

    @staticmethod
    def from_line(line: str) -> Instruction:
        move, units = map(str.strip, line.split(' '))
        units = int(units)

        return Instruction(move, units)


@log_time
def solution(inputs: List[Instruction]) -> int:
    horizontal, depth = 0,0
    for instruction in inputs:
        if instruction.move == "forward":
            horizontal += instruction.units

        if instruction.move == "up":
            depth -= instruction.units

        if instruction.move == "down":
            depth += instruction.units

    return horizontal * depth


@log_time
def solution2(inputs: List[Instruction]) -> int:
    horizontal, depth, aim = 0,0,0
    for instruction in inputs:
        if instruction.move == "forward":
            horizontal += instruction.units
            depth += aim * instruction.units

        if instruction.move == "up":
            aim -= instruction.units

        if instruction.move == "down":
            aim += instruction.units

    return horizontal * depth


def main():
    base_path = Path(__file__).parent
    tests = [TestCase.setup(base_path / "sample.txt", 150),
             TestCase.setup(base_path / "input.txt", 2120749),
             TestCase.setup(base_path / "input2.txt", 2036120)]

    test(solution, tests, Instruction.from_line)

    tests = [TestCase.setup(base_path / "sample.txt", 900),
             TestCase.setup(base_path / "input.txt", 2138382217),
             TestCase.setup(base_path / "input2.txt", 2015547716)]

    test(solution2, tests, Instruction.from_line)


if __name__ == "__main__":
    main()
