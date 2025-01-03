from year_2024.src import day12_plot_area as d12


test_input_filename = r"year_2024/tests/test_inputs/12_test_input.txt"
input_filename = r"year_2024/input/12_plot_area.txt"


def test_example():
    m = d12.ClassName(test_input_filename)
    assert m.fence_price() == 1930


def test_part1():
    m = d12.ClassName(input_filename)
    assert m.fence_price() == 1456082


def test_example_part2():
    m = d12.ClassName(test_input_filename)
    assert m.fence_price(part2=True) == 1206


def test_part2():
    m = d12.ClassName(input_filename)
    assert m.fence_price(part2=True) == 872382
