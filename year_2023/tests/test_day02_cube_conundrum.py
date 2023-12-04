from AdventOfCode.year_2023.src import day02_cube_conundrum as d02


def test_example():
    filename = r"year_2023/tests/test_inputs/02_test_input.txt"
    m = d02.CubeColors(filename)
    assert m.sum == 8


def test_part1():
    filename = r"year_2023/input/02_cube_conundrum.txt"
    m = d02.CubeColors(filename)
    assert m.sum == 2545


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/02_test_input.txt"
    m = d02.CubeColors(filename)
    assert m.power == 2286


def test_part2():
    filename = r"year_2023/input/02_cube_conundrum.txt"
    m = d02.CubeColors(filename)
    assert m.power == 78111
