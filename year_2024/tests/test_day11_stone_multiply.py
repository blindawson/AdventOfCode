from year_2024.src import day11_stone_multiply as d11


test_input_filename = r"year_2024/tests/test_inputs/11_test_input.txt"
input_filename = r"year_2024/input/11_stone_multiply.txt"


def test_example():
    m = d11.ClassName(test_input_filename)
    assert m.part1(6) == 22
    m = d11.ClassName(test_input_filename)
    assert m.part1(25) == 55312


def test_part1():
    m = d11.ClassName(input_filename)
    assert m.part1(25) == 186203


def test_part2():
    m = d11.ClassName(input_filename)
    assert m.part1(75) == 99
