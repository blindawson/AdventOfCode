from AdventOfCode.year_2023.src import day12_hot_springs as d12


def test_example():
    filename = r"year_2023/tests/test_inputs/12_test_input.txt"
    m = d12.Springs(filename)
    assert m.calc_arrangements() == 21


def test_part1():
    filename = r"year_2023/input/12_hot_springs.txt"
    m = d12.Springs(filename)
    assert m.calc_arrangements() == 7402


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/12_test_input.txt"
    m = d12.Springs(filename, part2=True)
    assert m.sum == 525152


def test_part2():
    filename = r"year_2023/input/12_hot_springs.txt"
    m = d12.Springs(filename)
    assert m.sum == 99
