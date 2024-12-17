from year_2024.src import day06_map_path as d06


test_input_filename = r"year_2024/tests/test_inputs/06_test_input.txt"
input_filename = r"year_2024/input/06_map_path.txt"


def test_example():
    m = d06.ClassName(test_input_filename)
    assert m.part1() == 41


def test_part1():
    m = d06.ClassName(input_filename)
    assert m.part1() == 4433


def test_example_part2():
    m = d06.ClassName(test_input_filename)
    assert m.part2() == 6


def test_part2():
    m = d06.ClassName(input_filename)
    assert m.part2() == 1516
