from AdventOfCode.year_2023.src import day21_map_expansion as d21
import numpy as np


def test_example():
    filename = r"year_2023/tests/test_inputs/21_test_input.txt"
    m = d21.Day21(filename)
    m.steps(6)
    assert m.count_plots() == 16


def test_part1():
    filename = r"year_2023/input/21_map_expansion.txt"
    m = d21.Day21(filename)
    m.steps(64)
    assert m.count_plots() == 3858


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/21_test_input.txt"
    m = d21.Day21(filename, part2=True)
    m.steps(6)
    assert m.count_plots() == 16
    m.steps(4)
    assert m.count_plots() == 50
    m.steps(40)
    assert m.count_plots() == 1594
    m.reset()
    assert m.extrapolate_steps(5000) == 16733044


def test_part2():
    filename = r"year_2023/input/21_map_expansion.txt"
    m = d21.Day21(filename, part2=True)
    assert m.extrapolate_steps(26501365) == 636350496972143
 