from AdventOfCode.year_2023.src import day17_dijkstra_directional as d17


def test_example():
    filename = r"year_2023/tests/test_inputs/17_test_input.txt"
    m = d17.Crucible(filename)
    assert m.min_heat_loss() == 102


def test_part1():
    filename = r"year_2023/input/17_dijkstra_directional.txt"
    m = d17.Crucible(filename)
    assert m.min_heat_loss() == 970


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/17_test_input.txt"
    m = d17.Crucible(filename, part2=True)
    assert m.part2() == 94


def test_part2():
    filename = r"year_2023/input/17_dijkstra_directional.txt"
    m = d17.Crucible(filename, part2=True)
    assert m.part2() == 99
