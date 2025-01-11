from year_2024.src import day13_claw_game as d13


test_input_filename = r"year_2024/tests/test_inputs/13_test_input.txt"
input_filename = r"year_2024/input/13_claw_game.txt"


def test_example():
    m = d13.ClassName(test_input_filename)
    assert m.run_input() == 480


def test_part1():
    m = d13.ClassName(input_filename)
    assert m.run_input() == 29522


def test_part2():
    m = d13.ClassName(input_filename)
    assert m.run_input(part2=True) == 101214869433312
