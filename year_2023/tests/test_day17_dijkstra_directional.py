from AdventOfCode.year_2023.src import day17_dijkstra_directional as d17


def test_example():
    filename = r"year_2023/tests/test_inputs/17_test_input.txt"
    m = d17.Crucible(filename)
    assert m.part1() == 99


def test_part1():
    filename = r"year_2023/input/17_dijkstra_directional.txt"
    m = d17.Crucible(filename)
    assert m.part1() == 99


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/17_test_input.txt"
    m = d17.Crucible(filename)
    assert m.part2() == 99


def test_part2():
    filename = r"year_2023/input/17_dijkstra_directional.txt"
    m = d17.Crucible(filename)
    assert m.part2() == 99
