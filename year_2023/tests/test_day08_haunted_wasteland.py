from AdventOfCode.year_2023.src import day08_haunted_wasteland as d08


def test_example():
    filename = r"year_2023/tests/test_inputs/08_test_input.txt"
    m = d08.ClassName(filename)
    assert m.total_steps == 6


def test_part1():
    filename = r"year_2023/input/08_haunted_wasteland.txt"
    m = d08.ClassName(filename)
    assert m.total_steps == 22411


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/08_test_input_part2.txt"
    m = d08.ClassName(filename, part2=True)
    assert m.total_steps == 6


def test_part2():
    filename = r"year_2023/input/08_haunted_wasteland.txt"
    m = d08.ClassName(filename, part2=True)
    assert m.total_steps == 11188774513823
