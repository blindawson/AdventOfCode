from AdventOfCode.year_2022.src import day14_regolith_reservoir as d14
import time

def test_example():
	filename = r'year_2022/tests/test_inputs/14_test_input.txt'
	r = d14.Regolith(filename)
	assert r.sand_amt == 24


def test_part1():
	filename = r'year_2022/input/14_regolith_reservoir.txt'
	r = d14.Regolith(filename)
	assert r.sand_amt == 655


def test_example_part2():
	filename = r'year_2022/tests/test_inputs/14_test_input.txt'
	r = d14.Regolith(filename, part2=True)
	assert r.sand_amt == 93


def test_part2():
	start_time = time.time()
	filename = r'year_2022/input/14_regolith_reservoir.txt'
	r = d14.Regolith(filename, part2=True)
	end_time = time.time()
	elapsed_time = end_time - start_time
	print(f"Execution time: {elapsed_time} seconds")
	assert r.sand_amt == 26484
