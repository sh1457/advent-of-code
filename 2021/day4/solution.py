from __future__ import annotations
from pathlib import Path
from typing import NamedTuple
from itertools import product

import numpy as np

from solver import TestCase, log_time, test


class Game(NamedTuple):
    inputs: list[int]
    boards: list[np.array]
    states: list[np.array]

    @staticmethod
    def from_data(data: list[str], board_size: int) -> Game:
        inputs = None
        boards = []
        states = []

        current_board = []
        for line in data:
            line = line.strip()
            if line == '':
                continue
            if inputs is None:
                inputs = list(map(int, line.split(',')))
                continue

            if len(current_board) < board_size:
                current_board.append(list(map(lambda x: int(x.strip()), line.split())))

            if len(current_board) == board_size:
                board = np.array(current_board)
                boards.append(board)
                states.append(np.ones_like(board))
                current_board = []

        if current_board:
            raise ValueError("Missing data")

        return Game(inputs=inputs, boards=boards, states=states)


@log_time
def solution(inputs: list[str]) -> None:
    board_size = 5
    game = Game.from_data(inputs, board_size)

    for draw in game.inputs:
        for board, state in zip(game.boards, game.states):
            for i, j in product(range(board_size), range(board_size)):
                if board[i,j] == draw:
                    state[i,j] = 0
                    break

            if 0 in np.sum(state, axis=0) or 0 in np.sum(state, axis=1):
                answer = np.sum(np.multiply(board, state)) * draw
                return answer


@log_time
def solution2(inputs: list[str]) -> None:
    board_size = 5
    game = Game.from_data(inputs, board_size)
    wins = {i: 0 for i in range(len(game.boards))}

    for draw in game.inputs:
        for index, (board, state) in enumerate(zip(game.boards, game.states)):
            if wins[index]:
                continue

            for i, j in product(range(board_size), range(board_size)):
                if board[i,j] == draw:
                    state[i,j] = 0
                    break

            if 0 in np.sum(state, axis=0) or 0 in np.sum(state, axis=1):
                wins[index] = 1

                if all(wins.values()):
                    answer = np.sum(np.multiply(board, state)) * draw
                    return answer


def main():
    base_path = Path(__file__).parent
    tests = [TestCase.setup(base_path / "sample.txt", 4512),
             TestCase.setup(base_path / "input.txt", 89001)]

    test(solution, tests)

    tests2 = [TestCase.setup(base_path / "sample.txt", 1924),
              TestCase.setup(base_path / "input.txt", 7296)]

    test(solution2, tests2)


if __name__ == "__main__":
    main()
