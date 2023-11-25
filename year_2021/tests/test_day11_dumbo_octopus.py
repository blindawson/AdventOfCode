import pandas as pd
from pandas._testing import assert_frame_equal
from AdventOfCode.year_2021.src import day11_dumbo_octopus as dd

test_data = dd.read_file(r'year_2021/tests/test_inputs/11_test_input.txt')
test_data_increment = dd.read_file(r'year_2021/tests/test_inputs/11_test_input_increment.txt')
test_data_increment2 = dd.read_file(r'year_2021/tests/test_inputs/11_test_input_increment2.txt')

def test_adjacent_point():
    grid_tf = test_data.copy()
    grid_tf.loc[:, :] = False
    grid_test1 = grid_tf.copy()
    grid_test1[1][0] = True
    grid_test1[1][1] = True
    grid_test1[0][1] = True
    assert_frame_equal(dd.adjacent_points(test_data, (0, 0)), grid_test1, check_dtype=False)


def test_increment_grid():
    grid = dd.increment_grid(test_data.copy())
    assert_frame_equal(grid, test_data_increment)


def test_flash_octopus():
    grid = dd.increment_grid(test_data.copy())
    grid = dd.increment_grid(grid)
    grid, flashes = dd.flash_octopus(grid)
    assert_frame_equal(grid, test_data_increment2)
    assert flashes == 35


def test_loop_steps():
    test_data = dd.read_file(r'year_2021/tests/test_inputs/11_test_input.txt')
    assert dd.loop_steps(test_data.copy(), 10) == 204
    assert dd.loop_steps(test_data.copy(), 100) == 1656
    

def test_all_flash():
    assert dd.all_flash(test_data.copy()) == 195