from AdventOfCode.year_2023.src import day13_point_of_incidence as d13


def test_example():
    filename = r"year_2023/tests/test_inputs/13_test_input.txt"
    m = d13.ClassName(filename)
    assert m.sum_grids() == 405


def test_part1():
    filename = r"year_2023/input/13_point_of_incidence.txt"
    m = d13.ClassName(filename)
    assert m.sum_grids() == 33975


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/13_test_input.txt"
    m = d13.ClassName(filename, part2=True)
    assert m.sum_grids() == 400


def test_part2():
    filename = r"year_2023/input/13_point_of_incidence.txt"
    m = d13.ClassName(filename, part2=True)
    assert m.sum_grids() == 29083
