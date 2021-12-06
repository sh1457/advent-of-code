from __future__ import annotations
from pathlib import Path
from typing import NamedTuple, List


from solver import TestCase, log_time, test


class Policy(NamedTuple):
    minimum: int
    maximum: int
    character: str
    password: str

    @staticmethod
    def from_line(line: str) -> Policy:
        policy, password = map(str.strip, line.split(':'))
        frequency, character = map(str.strip, policy.split(' '))
        minimum, maximum = map(int, frequency.split('-'))
        return Policy(minimum, maximum, character, password)


@log_time
def solution(policies: List[Policy]) -> int:
    valid_count = 0
    for policy in policies:
        if policy.minimum <= policy.password.count(policy.character) <= policy.maximum:
            valid_count += 1

    return valid_count


def main():
    base_path = Path(__file__).parent
    tests = [TestCase(base_path / 'sample.txt', 2),
             TestCase(base_path / 'input.txt', 666)]

    test(solution, tests, Policy.from_line)


if __name__ == '__main__':
    main()
