from AdventOfCode.year_2022.src import day17_pyroclastic_flow as d17


def test_example():
	filename = r'year_2022/tests/test_inputs/17_test_input.txt'
	t = d17.Tetris(filename)
	assert t.drop_blocks(2022) == 3068


def test_part1():
	filename = r'year_2022/input/17_pyroclastic_flow.txt'
	t = d17.Tetris(filename)
	assert t.drop_blocks(2022) == 3211


def test_example_part2():
	filename = r'year_2022/tests/test_inputs/17_test_input.txt'
	t = d17.Tetris(filename)
	assert t.drop_blocks(1000000000000) == 1514285714288


def test_part2():
	filename = r'year_2022/input/17_pyroclastic_flow.txt'
	t = d17.Tetris(filename)
	assert t.drop_blocks(1000000000000) == 1589142857183
