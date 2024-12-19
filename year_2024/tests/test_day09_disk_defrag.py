from year_2024.src import day09_disk_defrag as d09


test_input_filename = r"year_2024/tests/test_inputs/09_test_input.txt"
input_filename = r"year_2024/input/09_disk_defrag.txt"


def test_example():
    m = d09.Part1(test_input_filename)
    assert m.part1() == 1928


def test_part1():
    m = d09.Part1(input_filename)
    assert m.part1() == 6448989155953


def test_example_part2():
    m = d09.Part2(test_input_filename)
    assert m.part2() == 2858


def test_part2():
    m = d09.Part2(input_filename)
    assert m.part2() == 99
