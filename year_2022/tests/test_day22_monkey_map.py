from AdventOfCode.year_2022.src import day22_monkey_map as d22


def test_example():
    filename = r"year_2022/tests/test_inputs/22_test_input.txt"
    m = d22.MonkeyMap(filename)
    assert m.password() == 6032


def test_part1():
    filename = r"year_2022/input/22_monkey_map.txt"
    m = d22.MonkeyMap(filename)
    assert m.password() == 47462


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/22_test_input.txt"
    m = d22.MonkeyMap(filename, version="Part 2 Example")
    assert m.password() == 5031


def test_part2():
    filename = r"year_2022/input/22_monkey_map.txt"
    m = d22.MonkeyMap(filename, version="Part 2")
    assert m.password() == 137045
