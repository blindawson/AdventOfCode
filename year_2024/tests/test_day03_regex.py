from year_2024.src import day03_regex as d03


def test_example():
    filename = r"year_2024/tests/test_inputs/03_test_input.txt"
    m = d03.ClassName(filename)
    assert m.part1() == 161


def test_part1():
    filename = r"year_2024/input/03_regex.txt"
    m = d03.ClassName(filename)
    assert m.part1() == 187833789


def test_example_part2():
    filename = r"year_2024/tests/test_inputs/03_test_input_part2.txt"
    m = d03.ClassName(filename)
    assert m.part2() == 48


def test_part2():
    filename = r"year_2024/input/03_regex.txt"
    m = d03.ClassName(filename)
    assert m.part2() == 94455185
