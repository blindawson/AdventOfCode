from AdventOfCode.year_2023.src import day15_ascii_algorithm as d15


def test_example():
    filename = r"year_2023/tests/test_inputs/15_test_input.txt"
    m = d15.Hash(filename)
    assert m.add_hash() == 1320


def test_part1():
    filename = r"year_2023/input/15_ascii_algorithm.txt"
    m = d15.Hash(filename)
    assert m.add_hash() == 508498


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/15_test_input.txt"
    m = d15.Hash(filename)
    assert m.focusing_power() == 145


def test_part2():
    filename = r"year_2023/input/15_ascii_algorithm.txt"
    m = d15.Hash(filename)
    assert m.focusing_power() == 279116
