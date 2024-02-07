from AdventOfCode.year_2023.src import day18_inside_fill as d18


def test_example():
    filename = r"year_2023/tests/test_inputs/18_test_input.txt"
    m = d18.ClassName(filename)
    assert m.count_lava() == 62


def test_part1():
    filename = r"year_2023/input/18_inside_fill.txt"
    m = d18.ClassName(filename)
    assert m.count_lava() == 41019


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/18_test_input.txt"
    m = d18.ClassName(filename)
    assert m.part2() == 952408144115


def test_part2():
    filename = r"year_2023/input/18_inside_fill.txt"
    m = d18.ClassName(filename)
    assert m.part2() == 99
