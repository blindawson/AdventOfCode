from year_2024.src import day08_map_antinodes as d08


test_input_filename = r"year_2024/tests/test_inputs/08_test_input.txt"
input_filename = r"year_2024/input/08_map_antinodes.txt"


def test_example():
    m = d08.ClassName(test_input_filename)
    assert m.find_antinodes() == 14


def test_part1():
    m = d08.ClassName(input_filename)
    assert m.find_antinodes() == 265


def test_example_part2():
    m = d08.ClassName(test_input_filename)
    assert m.find_antinodes(part2=True) == 34


def test_part2():
    m = d08.ClassName(input_filename)
    assert m.find_antinodes(part2=True) == 962
