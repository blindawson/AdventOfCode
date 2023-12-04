from AdventOfCode.year_2023.src import day04_scratchcards as d04


def test_example():
    filename = r"year_2023/tests/test_inputs/04_test_input.txt"
    m = d04.Scratchcards(filename)
    assert m.sum_points == 13


def test_part1():
    filename = r"year_2023/input/04_scratchcards.txt"
    m = d04.Scratchcards(filename)
    assert m.sum_points == 25571


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/04_test_input.txt"
    m = d04.Scratchcards(filename)
    assert sum(m.card_count) == 30


def test_part2():
    filename = r"year_2023/input/04_scratchcards.txt"
    m = d04.Scratchcards(filename)
    assert sum(m.card_count) == 8805731
