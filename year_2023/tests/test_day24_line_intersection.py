from AdventOfCode.year_2023.src import day24_line_intersection as d24
from AdventOfCode.support import support


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
    m = d24.LineIntersection(filename, (7, 27, 7, 27))

    xv, yv, xy0 = m.part2(10)
    # Time and intersection location for two hailstones
    t1 = m.intersection_time(xy0, m.file_input[0], xv, yv)
    t2 = m.intersection_time(xy0, m.file_input[1], xv, yv)
    # Point at time
    p1 = m.hail_loc(m.file_input[0], t1)
    p2 = m.hail_loc(m.file_input[1], t2)

    # velocity between two intersection points
    v = [i / (t2 - t1) for i in support.subtract_tuples(p2, p1)]
    p0 = support.subtract_tuples(p1, [x * t1 for x in v])
    assert sum(p0) == 47


def test_part2():
    filename = r"year_2023/input/24_line_intersection.txt"
    m = d24.LineIntersection(filename, (7, 27, 7, 27))

    xv, yv, xy0 = m.part2(1000)
    # Time and intersection location for two hailstones
    t1 = m.intersection_time(xy0, m.file_input[0], xv, yv)
    t2 = m.intersection_time(xy0, m.file_input[1], xv, yv)
    # Point at time
    p1 = m.hail_loc(m.file_input[0], t1)
    p2 = m.hail_loc(m.file_input[1], t2)

    # velocity between two intersection points
    v = [i / (t2 - t1) for i in support.subtract_tuples(p2, p1)]
    p0 = support.subtract_tuples(p1, [x * t1 for x in v])

    assert sum(p0) == 600352360036779
