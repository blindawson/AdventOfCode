from AdventOfCode.year_2022.src import day15_beacon_exclusion_zone as d15


def test_example():
    filename = r"year_2022/tests/test_inputs/15_test_input.txt"
    b = d15.BeaconZone(filename)
    assert b.mark_searched(row=10) == 26


def test_part1():
    filename = r"year_2022/input/15_beacon_exclusion_zone.txt"
    b = d15.BeaconZone(filename)
    assert b.mark_searched(row=2000000) == 4737443


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/15_test_input.txt"
    assert d15.func(filename) == 99


def test_part2():
    filename = r"year_2022/input/15_beacon_exclusion_zone.txt"
    assert d15.func(filename) == 99
