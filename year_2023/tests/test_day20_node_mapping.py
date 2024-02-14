from AdventOfCode.year_2023.src import day20_node_mapping as d20


def test_example():
    filename = r"year_2023/tests/test_inputs/20_test_input.txt"
    m = d20.ClassName(filename)
    assert m.push_buttons() == 32000000


def test_example1():
    filename = r"year_2023/tests/test_inputs/20_test_input_2.txt"
    m = d20.ClassName(filename)
    assert m.push_buttons() == 11687500


def test_part1():
    filename = r"year_2023/input/20_node_mapping.txt"
    m = d20.ClassName(filename)
    assert m.push_buttons() == 861743850


def test_part2():
    filename = r"year_2023/input/20_node_mapping.txt"
    m = d20.ClassName(filename, 10000)
    m.push_buttons()
    assert (
        m.part2_list[0] * m.part2_list[2] * m.part2_list[3] * m.part2_list[1]
        == 247023644760071
    )
