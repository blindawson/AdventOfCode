from AdventOfCode.year_2023.src import day21_map_expansion as d21


def test_example():
    filename = r"year_2023/tests/test_inputs/21_test_input.txt"
    m = d21.Day21(filename)
    m.steps(6)
    assert m.count_plots() == 16


def test_part1():
    filename = r"year_2023/input/21_map_expansion.txt"
    m = d21.Day21(filename)
    m.steps(64)
    assert m.count_plots() == 3858


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/21_test_input.txt"
    m = d21.Day21(filename)
    assert m.part2() == 99


def test_part2():
    filename = r"year_2023/input/21_map_expansion.txt"
    m = d21.Day21(filename)
    assert m.part2() == 99
