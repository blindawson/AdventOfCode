from year_2024.src import day13_claw_game as d13


test_input_filename = r"year_2024/tests/test_inputs/13_test_input.txt"
input_filename = r"year_2024/input/13_claw_game.txt"


def test_example():
    m = d13.ClassName(test_input_filename)
    assert m.part1() == 480


def test_part1():
    m = d13.ClassName(input_filename)
    assert m.part1() == 29522


def test_example_part2():
    m = d13.ClassName(test_input_filename)
    assert m.part2() == 99


def test_part2():
    m = d13.ClassName(input_filename)
    assert m.part2() == 99
