from AdventOfCode.year_2023.src import day01_trebuchet as d01


def test_example():
    filename = r"year_2023/tests/test_inputs/01_test_input.txt"
    m = d01.ClassName(filename)
    assert m.sum == 142


def test_part1():
    filename = r"year_2023/input/01_trebuchet.txt"
    m = d01.ClassName(filename)
    assert m.sum == 54390


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/01_test_input_2.txt"
    m = d01.ClassName(filename, part2=True)
    assert m.sum == 281


def test_part2():
    filename = r"year_2023/input/01_trebuchet.txt"
    m = d01.ClassName(filename, part2=True)
    assert m.sum == 54277
