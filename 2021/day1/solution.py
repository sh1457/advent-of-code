from typing import List
from pathlib import Path

from solver import TestCase, log_time, test


@log_time
def solution(inputs: List[int]) -> int:
    counter = 0
    for elem, prev in zip(inputs[1:], inputs[:-1]):
        if elem > prev:
            counter += 1

    return counter


@log_time
def solution2(inputs: List[int]) -> int:
    counter = 0

    windows = [sum(inputs[i:i+3]) for i in range(0, len(inputs) - 2)]

    for elem, prev in zip(windows[1:], windows[:-1]):
        if elem > prev:
            counter += 1

    return counter


def main():
    base_path = Path(__file__).parent
    tests = [TestCase.setup(base_path / "sample.txt", 7),
             TestCase.setup(base_path / "input.txt", 1390)]

    test(solution, tests, lambda x: int(x.strip()))

    tests = [TestCase.setup(base_path / "sample.txt", 5),
             TestCase.setup(base_path / "input.txt", 1457)]

    test(solution2, tests, lambda x: int(x.strip()))


if __name__ == "__main__":
    main()
