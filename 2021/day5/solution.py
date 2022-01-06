from __future__ import annotations
from pathlib import Path
from typing import NamedTuple
from collections import Counter

from solver import TestCase, log_time, test


class Line(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int

    @staticmethod
    def from_data(data: str) -> Line:
        x1, y1, x2, y2 = map(int, data.strip().replace(' -> ', ',').split(','))
        return Line(x1=x1, y1=y1, x2=x2, y2=y2)

    def is_diagonal(self) -> bool:
        return True if (abs(self.x2-self.x1) and abs(self.y2-self.y1)) else False

    def get_straight_points(self) -> list[tuple[int, int]]:
        points = None
        x = abs(self.x2 - self.x1)
        y = abs(self.y2 - self.y1)

        if x:
            a,b = min(self.x2, self.x1), max(self.x2, self.x1)
            points = [(i,self.y1) for i in range(a,b+1)]

        if y:
            a,b = min(self.y2, self.y1), max(self.y2, self.y1)
            points = [(self.x1, j) for j in range(a,b+1)]

        return points

    def get_diagonal_points(self) -> list[tuple[int, int]]:
        points = None

        x_step = 1
        if self.x1 > self.x2:
            x_step = -1

        y_step = 1
        if self.y1 > self.y2:
            y_step = -1

        points = [(i,self.y1) for i in zip(range(self.x1, self.x2, x_step), range())]

        if y:
            a,b = min(self.y2, self.y1), max(self.y2, self.y1)
            points = [(self.x1, j) for j in range(a,b+1)]

        return points

@log_time
def solution(inputs: list[Line]) -> int:
    counts = Counter()
    for line in inputs:
        if not line.is_diagonal():
            for point in line.get_straight_points():
                counts[point] += 1

    overlaps = 0
    for val in counts.values():
        if val > 1:
            overlaps += 1

    return overlaps



@log_time
def solution2(inputs: list[Line]) -> int:
    counts = Counter()
    for line in inputs:
        if line.is_diagonal():
            for point in line.get_diagonal_points():
                counts[point] += 1
        else:
            for point in line.get_straight_points():
                counts[point] += 1

    overlaps = 0
    for val in counts.values():
        if val > 1:
            overlaps += 1

    return overlaps


def main():
    base_path = Path(__file__).parent
    tests = [TestCase.setup(base_path / "sample.txt", 5),
             TestCase.setup(base_path / "input.txt", 4745)]

    test(solution, tests, Line.from_data)

    tests2 = [TestCase.setup(base_path / "sample.txt", 12),
              TestCase.setup(base_path / "input.txt", 7296)]

    test(solution2, tests2[:1], Line.from_data)


if __name__ == "__main__":
    main()
