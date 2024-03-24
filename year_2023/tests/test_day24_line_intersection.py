from AdventOfCode.year_2023.src import day24_line_intersection as d24


def test_example():
    filename = r"year_2023/tests/test_inputs/24_test_input.txt"
    m = d24.LineIntersection(filename, (7, 27, 7, 27))
    assert m.compare_lines() == 2


def test_part1():
    filename = r"year_2023/input/24_line_intersection.txt"
    m = d24.LineIntersection(
        filename, (200000000000000, 400000000000000, 200000000000000, 400000000000000)
    )
    assert m.compare_lines() == 16172


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/24_test_input.txt"
    m = d24.LineIntersection(filename)
    assert m.part2() == 99


def test_part2():
    filename = r"year_2023/input/24_line_intersection.txt"
    m = d24.LineIntersection(filename)
    assert m.part2() == 99
