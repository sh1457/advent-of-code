from __future__ import annotations
from copy import copy
from typing import List
from pathlib import Path

from solver import TestCase, log_time, test


@log_time
def solution(inputs: List[List[int]]) -> None:
    majority = len(inputs) // 2

    counters = {i:j for i, j in enumerate(inputs[0])}
    for bits in inputs[1:]:
        for idx, bit in enumerate(bits):
            counters[idx] += bit

    gamma_bits = [1 if c >= majority else 0 for c in counters.values()]
    gamma = int(''.join(map(str, gamma_bits)), 2)

    epsilon_bits = [1 - bit for bit in gamma_bits]
    epsilon = int(''.join(map(str, epsilon_bits)), 2)

    return gamma * epsilon


def print_matrix(matrix: List[List[int]]):
    for r in matrix:
        for c in r:
            print(f"{c} ", end='')
        print()


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    t_matrix = [[] for n in matrix[0]]

    # print_matrix(matrix)

    for r in matrix:
        for i, c in enumerate(r):
            t_matrix[i].append(c)

    # print_matrix(t_matrix)

    return t_matrix


@log_time
def solution2(inputs: List[List[int]]) -> None:
    majority = len(inputs) // 2

    gamma_bits = [int(sum(bits) >= majority) for bits in transpose(inputs)]
    gamma = int(''.join(map(str, gamma_bits)), 2)

    epsilon_bits = [1 - bit for bit in gamma_bits]
    epsilon = int(''.join(map(str, epsilon_bits)), 2)

    return gamma * epsilon


@log_time
def solution3(inputs: List[List[int]]) -> None:
    o2_rating, co2_rating = None, None

    copy_inputs = copy(inputs)
    copy_inputs_2 = copy(inputs)
    for idx in range(len(inputs[0])):
        if o2_rating is None:
            n_ones = sum(transpose(copy_inputs)[idx])
            n_zeros = len(copy_inputs) - n_ones
            major_bit = 1 if n_ones >= n_zeros else 0
            copy_inputs = [num for num in copy_inputs if num[idx] == major_bit]
            if len(copy_inputs) == 1:
                o2_rating = copy_inputs[0]

        if co2_rating is None:
            n_ones = sum(transpose(copy_inputs_2)[idx])
            n_zeros = len(copy_inputs_2) - n_ones
            minor_bit = 0 if n_ones >= n_zeros else 1
            copy_inputs_2 = [num for num in copy_inputs_2 if num[idx] == minor_bit]
            if len(copy_inputs_2) == 1:
                co2_rating = copy_inputs_2[0]

    o2_rating = int(''.join(map(str, o2_rating)), 2)
    co2_rating = int(''.join(map(str, co2_rating)), 2)

    return o2_rating * co2_rating


def main():
    base_path = Path(__file__).parent
    tests = [TestCase.setup(base_path / "sample.txt", 198),
             TestCase.setup(base_path / "input.txt", 2648450)]

    test(solution, tests, lambda x: list(map(int, x.strip())))

    tests = [TestCase.setup(base_path / "sample.txt", 198),
             TestCase.setup(base_path / "input.txt", 2648450)]

    test(solution2, tests, lambda x: list(map(int, x.strip())))

    tests = [TestCase.setup(base_path / "sample.txt", 230),
             TestCase.setup(base_path / "input.txt", 2845944)]

    test(solution3, tests, lambda x: list(map(int, x.strip())))


if __name__ == "__main__":
    main()
