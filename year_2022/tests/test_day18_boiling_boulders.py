from AdventOfCode.year_2022.src import day18_boiling_boulders as d18


def test_example():
    filename = r"year_2022/tests/test_inputs/18_test_input.txt"
    r = d18.Lava(filename)
    assert r.sum_cube_faces() == 64


def test_part1():
    filename = r"year_2022/input/18_boiling_boulders.txt"
    r = d18.Lava(filename)
    assert r.sum_cube_faces() == 4282


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/18_test_input.txt"
    r = d18.Lava(filename, part2=True)
    assert r.sum_cube_faces() == 58


def test_part2():
    filename = r"year_2022/input/18_boiling_boulders.txt"
    r = d18.Lava(filename, part2=True)
    assert r.sum_cube_faces() == 2452
