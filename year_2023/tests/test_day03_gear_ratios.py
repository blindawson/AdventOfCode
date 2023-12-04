from AdventOfCode.year_2023.src import day03_gear_ratios as d03


def test_example():
    filename = r"year_2023/tests/test_inputs/03_test_input.txt"
    m = d03.Gear(filename)
    assert m.sum == 4361


def test_part1():
    filename = r"year_2023/input/03_gear_ratios.txt"
    m = d03.Gear(filename)
    assert m.sum == 509115


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/03_test_input.txt"
    m = d03.Gear(filename)
    assert m.gear_dict_sum == 467835


def test_part2():
    filename = r"year_2023/input/03_gear_ratios.txt"
    m = d03.Gear(filename)
    assert m.gear_dict_sum == 75220503
