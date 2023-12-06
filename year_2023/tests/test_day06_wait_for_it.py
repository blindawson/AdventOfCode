from AdventOfCode.year_2023.src import day06_wait_for_it as d06


def test_example():
    filename = r"year_2023/tests/test_inputs/06_test_input.txt"
    m = d06.BoatRace(filename)
    assert m.product == 288


def test_part1():
    filename = r"year_2023/input/06_wait_for_it.txt"
    m = d06.BoatRace(filename)
    assert m.product == 211904


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/06_test_input.txt"
    m = d06.BoatRace(filename)
    assert m.part2 == 71503


def test_part2():
    filename = r"year_2023/input/06_wait_for_it.txt"
    m = d06.BoatRace(filename)
    assert m.part2 == 43364472
