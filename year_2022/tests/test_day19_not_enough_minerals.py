from AdventOfCode.year_2022.src import day19_not_enough_minerals as d19
from AdventOfCode.support import support


def test_example():
    filename = r"year_2022/tests/test_inputs/19_test_input.txt"
    blueprints = []
    for b in support.read_input(filename):
        blueprints.append(d19.read_blueprint(b))
    assert d19.Mining(blueprints, time_limit=24).quality_level == 33


def test_part1():
    filename = r"year_2022/input/19_not_enough_minerals.txt"
    blueprints = []
    for b in support.read_input(filename):
        blueprints.append(d19.read_blueprint(b))
    m = d19.Mining(blueprints, time_limit=24)
    assert m.quality_level == 1044
    # 1043 too low


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/19_test_input.txt"
    assert d19.func(filename) == 99


def test_part2():
    filename = r"year_2022/input/19_not_enough_minerals.txt"
    assert d19.func(filename) == 99
