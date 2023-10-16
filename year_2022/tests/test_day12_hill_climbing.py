import numpy as np

from AdventOfCode.year_2022.src import day12_hill_climbing as d12
from AdventOfCode.support import support


def test_sample_inputs():
    hill_map = support.read_input(
        r"year_2022/tests/test_inputs/12_hill_climbing.txt", flavor="str_grid"
    )
    hill_map = np.array([np.array(xi) for xi in hill_map])
    d = d12.Dijkstra_grid(hill_map)
    assert d.path_length == 31


def test_part1():
    hill_map = support.read_input(
        r"year_2022/input/12_hill_climbing.txt", flavor="str_grid"
    )
    hill_map = np.array([np.array(xi) for xi in hill_map])
    assert d12.Dijkstra_grid(hill_map).path_length == 472


def test_sample_inputs_part2():
    hill_map = support.read_input(
        r"year_2022/tests/test_inputs/12_hill_climbing.txt", flavor="str_grid"
    )
    hill_map = np.array([np.array(xi) for xi in hill_map])
    d = d12.Dijkstra_grid(hill_map, part2=True)
    assert d.path_length - 1 == 29


def test_part2():
    hill_map = support.read_input(
        r"year_2022/input/12_hill_climbing.txt", flavor="str_grid"
    )
    hill_map = np.array([np.array(xi) for xi in hill_map])
    assert d12.Dijkstra_grid(hill_map, part2=True).path_length - 1 == 465
