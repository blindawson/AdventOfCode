from AdventOfCode.year_2023.src import day25_network_diagram as d25
import math
from itertools import combinations


def test_example():
    filename = r"year_2023/tests/test_inputs/25_test_input.txt"
    m = d25.Day25(filename)

    group_sizes = m.cut_wires()
    group_prod = math.prod(group_sizes)
    assert group_prod == 54


def test_part1():
    filename = r"year_2023/input/25_network_diagram.txt"
    m = d25.Day25(filename)

    group_sizes = m.cut_wires()
    group_prod = math.prod(group_sizes)
    assert group_prod == 601344
