from AdventOfCode.year_2022.src import day19_not_enough_minerals as d19
from AdventOfCode.support import support


def test_example():
    filename = r"year_2022/tests/test_inputs/19_test_input.txt"
    for b in support.read_input(filename):
    	blueprint = d19.Blueprint(b)
    assert d19.Mining(blueprints, time_limit=24).max_geodes == 33


def test_part1():
    filename = r"year_2022/input/19_not_enough_minerals.txt"
    assert d19.func(filename) == 99


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/19_test_input.txt"
    assert d19.func(filename) == 99


def test_part2():
    filename = r"year_2022/input/19_not_enough_minerals.txt"
    assert d19.func(filename) == 99
