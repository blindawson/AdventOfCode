from AdventOfCode.year_2023.src import day19_rule_tree as d19


def test_example():
    filename = r"year_2023/tests/test_inputs/19_test_input.txt"
    m = d19.ClassName(filename)
    assert m.process_parts() == 19114


def test_part1():
    filename = r"year_2023/input/19_rule_tree.txt"
    m = d19.ClassName(filename)
    assert m.process_parts() == 449531


def test_example_part2():
    filename = r"year_2023/tests/test_inputs/19_test_input.txt"
    m = d19.ClassName(filename)
    assert m.part2() == 99


def test_part2():
    filename = r"year_2023/input/19_rule_tree.txt"
    m = d19.ClassName(filename)
    assert m.part2() == 99
