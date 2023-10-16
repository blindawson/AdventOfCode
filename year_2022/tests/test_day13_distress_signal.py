from AdventOfCode.year_2022.src import day13_distress_signal as d13


def test_sample_inputs():
    filename = r"year_2022/tests/test_inputs/13_test_input.txt"
    assert d13.right_order_sum(filename) == 13


def test_part1():
    filename = r"year_2022/input/13_distress_signal.txt"
    # 5910 too low
    assert d13.right_order_sum(filename) == 6656