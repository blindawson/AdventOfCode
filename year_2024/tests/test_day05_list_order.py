from year_2024.src import day05_list_order as d05


def test_example():
    filename = r"year_2024/tests/test_inputs/05_test_input.txt"
    m = d05.ClassName(filename)
    assert m.part1() == 143


def test_part1():
    filename = r"year_2024/input/05_list_order.txt"
    m = d05.ClassName(filename)
    assert m.part1() == 5452


def test_example_part2():
    filename = r"year_2024/tests/test_inputs/05_test_input.txt"
    m = d05.ClassName(filename)
    assert m.part2() == 123


def test_part2():
    filename = r"year_2024/input/05_list_order.txt"
    m = d05.ClassName(filename)
    assert m.part2() == 4598
