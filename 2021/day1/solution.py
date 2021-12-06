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


def main():
    base_path = Path(__file__).parent
    tests = [TestCase.setup(base_path / "sample.txt", 7),
             TestCase.setup(base_path / "input.txt", 1389)]

    test(solution, tests)


if __name__ == "__main__":
    main()
