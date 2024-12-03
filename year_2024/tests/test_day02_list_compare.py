from year_2024.src import day02_list_compare as d02


def test_example():
    filename = r"year_2024/tests/test_inputs/02_test_input.txt"
    m = d02.ClassName(filename)
    assert m.part1() == 2


def test_part1():
    filename = r"year_2024/input/02_list_compare.txt"
    m = d02.ClassName(filename)
    assert m.part1() == 383


def test_example_part2():
    filename = r"year_2024/tests/test_inputs/02_test_input.txt"
    m = d02.ClassName(filename)
    assert m.part2() == 4


def test_part2():
    filename = r"year_2024/input/02_list_compare.txt"
    m = d02.ClassName(filename)
    assert m.part2() == 436
