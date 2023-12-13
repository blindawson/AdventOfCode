from AdventOfCode.year_2023.src import day09_mirage_maintenance as d09


def test_example():
    filename = r"year_2023/tests/test_inputs/09_test_input.txt"
    m = d09.Mirage(filename)
    assert m.next_num == 114


def test_part1():
    filename = r"year_2023/input/09_mirage_maintenance.txt"
    m = d09.Mirage(filename)
    assert m.next_num == 1637452029


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/09_test_input.txt"
    m = d09.Mirage(filename)
    assert m.prev_num == 2


def test_part2():
    filename = r"year_2023/input/09_mirage_maintenance.txt"
    m = d09.Mirage(filename)
    assert m.prev_num == 908
