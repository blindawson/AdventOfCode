from year_2024.src import day04_wordsearch as d04


def test_example():
    filename = r"year_2024/tests/test_inputs/04_test_input.txt"
    m = d04.ClassName(filename)
    assert m.part1() == 18


def test_part1():
    filename = r"year_2024/input/04_wordsearch.txt"
    m = d04.ClassName(filename)
    assert m.part1() == 2406


def test_example_part2():
    filename = r"year_2024/tests/test_inputs/04_test_input.txt"
    m = d04.ClassName(filename)
    assert m.part2() == 9


def test_part2():
    filename = r"year_2024/input/04_wordsearch.txt"
    m = d04.ClassName(filename)
    assert m.part2() == 1807
