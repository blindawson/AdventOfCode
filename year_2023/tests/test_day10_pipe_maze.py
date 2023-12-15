from AdventOfCode.year_2023.src import day10_pipe_maze as d10


def test_example():
    filename = r"year_2023/tests/test_inputs/10_test_input.txt"
    m = d10.PipeMaze(filename)
    assert m.loop_len == 8


def test_part1():
    filename = r"year_2023/input/10_pipe_maze.txt"
    m = d10.PipeMaze(filename)
    assert m.loop_len == 7102


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/10_test_input2.txt"
    m = d10.PipeMaze(filename)
    assert m.count_spaces() == 8


def test_part2():
    filename = r"year_2023/input/10_pipe_maze.txt"
    m = d10.PipeMaze(filename)
    assert m.count_spaces() == 363
