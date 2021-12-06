from pathlib import Path
from typing import Callable, List, NamedTuple, Any

import click


def read_input(input_path: str) -> List[str]:
    path = Path(input_path)
    input_data = None
    with open(path, 'r') as fp:
        input_data = fp.readlines()

    return input_data


class TestCase(NamedTuple):
    input_path: str
    output: Any


def test(func: Callable, test: List[TestCase]):
    if not isinstance(test, list):
        test = [test]

    fail_counter = 0
    for test_case in test:
        actual_output = func(read_input(test_case.input_path))
        try:
            assert actual_output == test_case.output, f"Test case failed\nExpected {test_case.output} but got {actual_output}"
        except AssertionError:
            fail_counter += 1

    print(f"Ran {len(test)} tests.")
    if fail_counter:
        print(f"{fail_counter} tests failed.")


def run_solution(path: Path):
    from subprocess import Popen, PIPE

    process = Popen(['python', path], stdin=PIPE, stdout=PIPE)
    stdout, _ = process.communicate()

    print(stdout.decode('utf-8'))


@click.command()
@click.option('--problem', '-p')
def solve(problem: str):
    year, day = problem[:4], problem[5:]
    print(year, day)

    path = Path(__file__).parent / year / day

    if not path.exists():
        raise ValueError("Problem not solved yet.")

    solution_path = None
    for _path in path.glob("*solution.py"):
        solution_path = _path
        break

    if solution_path is None:
        raise ValueError("Problem not solved yet.")

    run_solution(solution_path)
