from pathlib import Path

import pytest
from pytest import param

from minesweeper.reader import Field, parse_input


def get_resource(resource_name):
    root = Path(r"C:\dev\projects\_codingdojo\minesweeper\tests\resources")
    return root / resource_name


@pytest.mark.parametrize(
    "input_file, output_file",
    [
        param(get_resource("input_0.txt"), get_resource("output_0.txt"), id="input0"),
    ],
)
def test_field_calculation(input_file, output_file):
    with open(input_file, "r") as f:
        input_string = f.read()

    field = Field.from_string(input_string)
    with open(output_file, "r") as f:
        output_string = f.read()

    assert str(field) == output_string


@pytest.mark.parametrize(
    "input_file, output_file",
    [
        param(get_resource("input_1.txt"), get_resource("output_1.txt"), id="input0"),
        param(get_resource("input_2.txt"), get_resource("output_2.txt"), id="input0"),
    ],
)
def test_input_and_output(input_file, output_file):
    with open(input_file, "r") as f:
        output = parse_input(f)

    with open(output_file, "r") as f:
        output_string = f.read()

    assert output == output_string
