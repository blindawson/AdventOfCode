from AdventOfCode.year_2022.src import day20_grove_positioning_system as d20


def test_example():
	filename = r'year_2022/tests/test_inputs/20_test_input.txt'
	p = d20.Positioning(filename)
	assert p.find_groves() == 3


def test_part1():
	filename = r'year_2022/input/20_grove_positioning_system.txt'
	p = d20.Positioning(filename)
	assert p.find_groves() == 4914


def test_example_part2():
	filename = r'year_2022/tests/test_inputs/20_test_input.txt'
	p = d20.Positioning(filename, part2=True)
	assert p.find_groves() == 1623178306


def test_part2():
	filename = r'year_2022/input/20_grove_positioning_system.txt'
	p = d20.Positioning(filename, part2=True)
	assert p.find_groves() == 7973051839072
