from year_2024.src import day01_list_compare as d01


def test_example():
    filename = r"year_2024/tests/test_inputs/01_test_input.txt"
    m = d01.ClassName(filename)
    assert m.part1() == 11


def test_part1():
    filename = r"year_2024/input/01_list_compare.txt"
    m = d01.ClassName(filename)
    assert m.part1() == 2769675


def test_example_part2():
    filename = r"year_2024/tests/test_inputs/01_test_input.txt"
    m = d01.ClassName(filename)
    assert m.part2() == 31


def test_part2():
    filename = r"year_2024/input/01_list_compare.txt"
    m = d01.ClassName(filename)
    assert m.part2() == 24643097
