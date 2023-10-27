from AdventOfCode.year_2022.src import day16_proboscidea_volcanium as d16


def test_example():
    filename = r"year_2022/tests/test_inputs/16_test_input.txt"
    v = d16.Volcano(filename)
    current_valve = v.find_valve("AA")
    v.explore_path(v.flow_valves, current_valve)
    assert v.max_pressure == 1651


def test_part1():
    filename = r"year_2022/input/16_proboscidea_volcanium.txt"
    v = d16.Volcano(filename)
    current_valve = v.find_valve("AA")
    v.explore_path(v.flow_valves, current_valve)
    assert v.max_pressure == 1896


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/16_test_input.txt"
    v = d16.Volcano(filename)
    current_valve = v.find_valve("AA")
    v.explore_path_part2(
        v.flow_valves, current_valve1=current_valve, current_valve2=current_valve
    )
    assert v.max_pressure == 1707


def test_part2():
    filename = r"year_2022/input/16_proboscidea_volcanium.txt"
    v = d16.Volcano(filename)
    current_valve = v.find_valve("AA")
    v.explore_path_part2(
        v.flow_valves, current_valve1=current_valve, current_valve2=current_valve
    )
    assert v.max_pressure == 1707
