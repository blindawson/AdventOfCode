from AdventOfCode.year_2023.src import day22_tetris as d22


def test_example():
    filename = r"year_2023/tests/test_inputs/22_test_input.txt"
    m = d22.Tetris(filename)
    assert m.disintegrate_blocks()[0] == 5


def test_part1():
    filename = r"year_2023/input/22_tetris.txt"
    m = d22.Tetris(filename)
    assert m.disintegrate_blocks()[0] == 522


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/22_test_input.txt"
    m = d22.Tetris(filename)
    assert m.disintegrate_blocks()[1] == 7


def test_part2():
    filename = r"year_2023/input/22_tetris.txt"
    m = d22.Tetris(filename)
    assert m.disintegrate_blocks()[1] == 83519
