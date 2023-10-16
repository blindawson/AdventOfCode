from AdventOfCode.year_2022.src import day13_distress_signal as d13


def test_sample_inputs():
    filename = r"year_2022/tests/test_inputs/13_test_input.txt"
    assert d13.right_order_sum(filename) == 13


def test_part1():
    filename = r"year_2022/input/13_distress_signal.txt"
    assert d13.right_order_sum(filename) == 6656
    
    
def test_sample_part2():
    filename = r"year_2022/tests/test_inputs/13_test_input.txt"
    packets = d13.order_all(filename)
    div_packet1_index = packets.index([[2]]) + 1
    div_packet2_index = packets.index([[6]]) + 1
    assert div_packet1_index * div_packet2_index == 140
    

def test_part2():
    filename = r"year_2022/input/13_distress_signal.txt"
    packets = d13.order_all(filename)
    div_packet1_index = packets.index([[2]]) + 1
    div_packet2_index = packets.index([[6]]) + 1
    assert div_packet1_index * div_packet2_index == 19716