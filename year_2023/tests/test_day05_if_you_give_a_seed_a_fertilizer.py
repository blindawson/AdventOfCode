from AdventOfCode.year_2023.src import day05_if_you_give_a_seed_a_fertilizer as d05


def test_example():
    filename = r"year_2023/tests/test_inputs/05_test_input.txt"
    m = d05.Seed(filename)
    assert m.min_loc == 35


def test_part1():
    filename = r"year_2023/input/05_if_you_give_a_seed_a_fertilizer.txt"
    m = d05.Seed(filename)
    assert m.min_loc == 322500873


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/05_test_input.txt"
    m = d05.Seed(filename)
    assert m.min_loc_part2 == 46


def test_part2():
    filename = r"year_2023/input/05_if_you_give_a_seed_a_fertilizer.txt"
    m = d05.Seed(filename)
    assert m.min_loc_part2 == 46
