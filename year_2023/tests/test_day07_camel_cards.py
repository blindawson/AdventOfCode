from AdventOfCode.year_2023.src import day07_camel_cards as d07


def test_example():
    filename = r"year_2023/tests/test_inputs/07_test_input.txt"
    m = d07.ClassName(filename)
    assert m.sum == 6440


def test_part1():
    filename = r"year_2023/input/07_camel_cards.txt"
    m = d07.ClassName(filename)
    assert m.sum == 253954294


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/07_test_input.txt"
    m = d07.ClassName(filename, jokers_wild=True)
    assert m.sum == 5905


def test_part2():
    filename = r"year_2023/input/07_camel_cards.txt"
    m = d07.ClassName(filename, jokers_wild=True)
    assert m.sum == 254837398
