from AdventOfCode.year_2022.src import day24_blizzard_basin as d24


def test_example():
	filename = r'year_2022/tests/test_inputs/24_test_input.txt'
	m = d24.Blizzard(filename)
	assert m.time + 1 == 18


def test_part1():
	filename = r'year_2022/input/24_blizzard_basin.txt'
	m = d24.Blizzard(filename)
	assert m.time + 1 == 297


def test_example_part2():
	filename = r'year_2022/tests/test_inputs/24_test_input.txt'
	assert d24.func(filename) == 99


def test_part2():
	filename = r'year_2022/input/24_blizzard_basin.txt'
	assert d24.func(filename) == 99
