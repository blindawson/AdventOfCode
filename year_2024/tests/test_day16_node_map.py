from year_2024.src import day16_node_map as d16


test_input_filename = r"year_2024/tests/test_inputs/16_test_input.txt"
test_input_filename2 = r"year_2024/tests/test_inputs/16_test_input2.txt"
input_filename = r"year_2024/input/16_node_map.txt"


def test_example1():
    m = d16.ClassName(test_input_filename)
    assert m.part1() == 7036


def test_example2():
    m = d16.ClassName(test_input_filename2)
    assert m.part1() == 11048


def test_part1():
    m = d16.ClassName(input_filename)
    assert m.part1() == 99


def test_example_part2():
    m = d16.ClassName(test_input_filename)
    assert m.part2() == 99


def test_part2():
    m = d16.ClassName(input_filename)
    assert m.part2() == 99
