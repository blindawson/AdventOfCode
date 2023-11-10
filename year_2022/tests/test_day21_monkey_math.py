from AdventOfCode.year_2022.src import day21_monkey_math as d21


def test_example():
	filename = r'year_2022/tests/test_inputs/21_test_input.txt'
	m = d21.MonkeyMath(filename)
	assert m.ans["root"] == 152


def test_part1():
	filename = r'year_2022/input/21_monkey_math.txt'
	m = d21.MonkeyMath(filename)
	assert m.ans["root"] == 145167969204648


def test_example_part2():
	filename = r'year_2022/tests/test_inputs/21_test_input.txt'
	m = d21.MonkeyMath(filename, part2=True)
	assert m.solution == 301


def test_part2():
	filename = r'year_2022/input/21_monkey_math.txt'
	m = d21.MonkeyMath(filename, part2=True)
	assert m.solution == 3330805295850
