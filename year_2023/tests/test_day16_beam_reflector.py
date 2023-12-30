from AdventOfCode.year_2023.src import day16_beam_reflector as d16


def test_example():
    filename = r"year_2023/tests/test_inputs/16_test_input.txt"
    m = d16.BeamReflector(filename)
    assert m.move_beam() == 46


def test_part1():
    filename = r"year_2023/input/16_beam_reflector.txt"
    m = d16.BeamReflector(filename)
    assert m.move_beam() == 8116


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/16_test_input.txt"
    m = d16.BeamReflector(filename)
    assert m.find_beam() == 51


def test_part2():
    filename = r"year_2023/input/16_beam_reflector.txt"
    m = d16.BeamReflector(filename)
    assert m.find_beam() == 8383
