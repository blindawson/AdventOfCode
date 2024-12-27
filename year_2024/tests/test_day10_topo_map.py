from year_2024.src import day10_topo_map as d10


test_input_filename = r"year_2024/tests/test_inputs/10_test_input.txt"
input_filename = r"year_2024/input/10_topo_map.txt"


def test_example():
    m = d10.ClassName(test_input_filename)
    assert m.part1() == 36


def test_part1():
    m = d10.ClassName(input_filename)
    assert m.part1() == 582


def test_example_part2():
    m = d10.ClassName(test_input_filename)
    assert m.part2() == 81


def test_part2():
    m = d10.ClassName(input_filename)
    assert m.part2() == 1302
