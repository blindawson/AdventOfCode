from AdventOfCode.year_2023.src import day11_cosmic_expansion as d11


def test_example():
    filename = r"year_2023/tests/test_inputs/11_test_input.txt"
    m = d11.Galaxy(filename)
    assert m.sum == 374


def test_part1():
    filename = r"year_2023/input/11_cosmic_expansion.txt"
    m = d11.Galaxy(filename)
    assert m.sum == 9233514


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/11_test_input.txt"
    m = d11.Galaxy(filename, expansion=100)
    assert m.sum == 8410


def test_part2():
    filename = r"year_2023/input/11_cosmic_expansion.txt"
    m = d11.Galaxy(filename, expansion=1000000)
    assert m.sum == 363293506944
