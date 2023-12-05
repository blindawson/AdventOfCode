from AdventOfCode.year_2023.src import day05_if_you_give_a_seed_a_fertilizer as d05


def test_example():
    filename = r"year_2023/tests/test_inputs/05_test_input.txt"
    m = d05.Seed(filename)
    assert m.min_loc == 35
    # Range 1 in Range 2
    assert m.split_range((50, 60), (50, 60)) == [(50, 60)]
    assert m.split_range((50, 60), (40, 70)) == [(50, 60)]
    # Range 2 in Range 1
    assert m.split_range((48, 62), (50, 60)) == [(48, 49), (50, 60), (61, 62)]
    assert m.split_range((49, 61), (50, 60)) == [(49, 49), (50, 60), (61, 61)]
    # Range 1 then Range 2
    assert m.split_range((49, 60), (50, 60)) == [(49, 49), (50, 60)]
    assert m.split_range((48, 60), (50, 60)) == [(48, 49), (50, 60)]
    assert m.split_range((48, 59), (50, 60)) == [(48, 49), (50, 59)]
    # Range 2 then Range 1
    assert m.split_range((49, 60), (40, 50)) == [(49, 50), (51, 60)]
    assert m.split_range((48, 60), (40, 50)) == [(48, 50), (51, 60)]
    assert m.split_range((48, 59), (40, 50)) == [(48, 50), (51, 59)]


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
    assert m.min_loc_part2 == 108956227
