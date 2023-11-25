from AdventOfCode.year_2022.src import day25_full_of_hot_air as d25


def test_example():
    filename = r"year_2022/tests/test_inputs/25_test_input.txt"
    m = d25.HotAir(filename)
    assert m.sum_input() == 4890
    assert m.convert_to_num5(1) == "1"
    assert m.convert_to_num5(3) == "1="
    assert m.convert_to_num5(9) == "2-"
    assert m.convert_to_num5(20) == "1-0"
    assert m.convert_to_num5(2022) == "1=11-2"
    assert m.convert_to_num5(m.sum_input()) == "2=-1=0"


def test_part1():
    filename = r"year_2022/input/25_full_of_hot_air.txt"
    m = d25.HotAir(filename)
    assert m.convert_to_num5(m.sum_input()) == "2-10==12-122-=1-1-22"


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/25_test_input.txt"
    assert d25.HotAir(filename) == 99


def test_part2():
    filename = r"year_2022/input/25_full_of_hot_air.txt"
    assert d25.HotAir(filename) == 99
