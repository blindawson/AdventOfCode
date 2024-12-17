from year_2024.src import day07_math_operators as d07


test_input_filename = r"year_2024/tests/test_inputs/07_test_input.txt"
input_filename = r"year_2024/input/07_math_operators.txt"


def test_example():
    m = d07.ClassName(test_input_filename)
    assert m.part1() == 3749


def test_part1():
    m = d07.ClassName(input_filename)
    assert m.part1() == 882304362421


def test_example_part2():
    m = d07.ClassName(test_input_filename)
    assert m.part2() == 11387


def test_part2():
    m = d07.ClassName(input_filename)
    assert m.part2() == 145149066755184
