from AdventOfCode.year_2023.src import day23_maze as d23


def test_example():
    filename = r"year_2023/tests/test_inputs/23_test_input.txt"
    m = d23.Maze(filename)
    assert m.follow_path((0, 1), m.explored.copy()).sum()-1 == 94


def test_part1():
    filename = r"year_2023/input/23_maze.txt"
    m = d23.Maze(filename)
    assert m.follow_path((0, 1), m.explored.copy()).sum()-1 == 2186


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/23_test_input.txt"
    m = d23.Maze(filename, part2=True)
    assert m.follow_path((0, 1), m.explored.copy()).sum()-1 == 154


def test_part2():
    filename = r"year_2023/input/23_maze.txt"
    m = d23.Maze(filename, part2=True)
    assert m.follow_path((0, 1), m.explored.copy()).sum()-1 == 154
    # 6239 too low