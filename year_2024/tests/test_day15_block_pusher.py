from year_2024.src import day15_block_pusher as d15


test_input_filename = r"year_2024/tests/test_inputs/15_test_input.txt"
input_filename = r"year_2024/input/15_block_pusher.txt"


def test_example():
    m = d15.ClassName(test_input_filename)
    m.move_robot_all_instructions()
    assert m.sum_box_gps() == 10092


def test_part1():
    m = d15.ClassName(input_filename)
    m.move_robot_all_instructions()
    assert m.sum_box_gps() == 1442192


def test_example_part2():
    m = d15.ClassName(test_input_filename, part2=True)
    m.move_robot_all_instructions()
    assert m.sum_box_gps() == 9021


def test_part2():
    m = d15.ClassName(input_filename, part2=True)
    m.move_robot_all_instructions()
    assert m.sum_box_gps() == 99
    # 1448462 too high