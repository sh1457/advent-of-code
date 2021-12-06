from pathlib import Path
from typing import Callable, List, NamedTuple, Any, Union
from functools import wraps
import subprocess
import sys
import time

import click


def read_input(input_path: Path, func: Callable=None) -> List[str]:
    input_data = None
    with open(input_path, 'r') as fp:
        if func is not None:
            input_data = list(map(func, fp.readlines()))
        else:
            input_data = fp.readlines()

    return input_data


class TestCase(NamedTuple):
    input_path: Union[str, Path]
    output: Any

    @staticmethod
    def setup(input_path: Union[str, Path], output: Any):
        input_path = input_path if isinstance(input_path, Path) else Path(input_path).resolve()
        return TestCase(input_path, output)


def log_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__!r} executed in {end_time-start_time:.4f}s")
        return result
    return wrapper


def test(func: Callable, test: List[TestCase], line_processor: Callable=None):
    if not isinstance(test, list):
        test = [test]

    fail_counter = 0
    for test_case in test:
        if line_processor is not None:
            actual_output = func(read_input(test_case.input_path, line_processor))
        else:
            actual_output = func(read_input(test_case.input_path))

        try:
            assert actual_output == test_case.output, f"|-- Test case failed\n\t|-- Expected {test_case.output} but got {actual_output}"
        except AssertionError as err:
            fail_counter += 1
            print(err)

    print(f"Ran {len(test)} tests.")
    if fail_counter:
        print(f"{len(test) - fail_counter} tests passed.")
        print(f"{fail_counter} tests failed.")
    else:
        print(f"All tests pass.")


def run_solution(path: Path):
    subprocess.run([sys.executable, path], stdout=sys.stdout, stderr=sys.stderr)


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
