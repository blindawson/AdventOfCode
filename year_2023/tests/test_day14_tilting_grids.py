from AdventOfCode.year_2023.src import day14_tilting_grids as d14


def test_example():
    filename = r"year_2023/tests/test_inputs/14_test_input.txt"
    m = d14.ClassName(filename)
    assert m.calc_load() == 136


def test_part1():
    filename = r"year_2023/input/14_tilting grids.txt"
    m = d14.ClassName(filename)
    assert m.calc_load() == 112046


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/14_test_input.txt"
    m = d14.ClassName(filename, loop_length=1000000000)
    assert m.calc_load() == 64


def test_part2():
    filename = r"year_2023/input/14_tilting grids.txt"
    m = d14.ClassName(filename, loop_length=1000000000)
    assert m.calc_load() == 104619
