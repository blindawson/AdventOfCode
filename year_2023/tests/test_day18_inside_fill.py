from AdventOfCode.year_2023.src import day18_inside_fill as d18


def test_example():
    filename = r"year_2023/tests/test_inputs/18_test_input.txt"
    m = d18.ClassName(filename)
    assert m.total_points == 62


def test_part1():
    filename = r"year_2023/input/18_inside_fill.txt"
    m = d18.ClassName(filename)
    assert m.total_points == 41019


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/18_test_input.txt"
    m = d18.ClassName(filename, part2=True)
    assert m.total_points == 952408144115


def test_part2():
    filename = r"year_2023/input/18_inside_fill.txt"
    m = d18.ClassName(filename, part2=True)
    assert m.total_points == 96116995735219
