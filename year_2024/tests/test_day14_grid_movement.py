from year_2024.src import day14_grid_movement as d14


test_input_filename = r"year_2024/tests/test_inputs/14_test_input.txt"
input_filename = r"year_2024/input/14_grid_movement.txt"


def test_example():
    m = d14.ClassName(test_input_filename, width=11, height=7, seconds=100)
    assert m.part1(100) == 12


def test_part1():
    m = d14.ClassName(input_filename, width=101, height=103, seconds=100)
    assert m.part1(100) == 218619324
