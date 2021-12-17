import pandas as pd
import numpy as np


def read_file(file):
    open_file = open(file).read().splitlines()
    return pd.DataFrame([list(x) for x in open_file]).astype(int)


def adjacent_points(grid, point):
    x, y = point
    x_max = grid.shape[0] - 1
    y_max = grid.shape[1] - 1
    adjacent = [(x-1, y-1),
                (x, y-1),
                (x+1, y-1),
                (x-1, y),
                (x+1, y),
                (x-1, y+1),
                (x, y+1),
                (x+1, y+1)]
    adjacent[:] = [i for i in adjacent if i[0] >= 0]
    adjacent[:] = [i for i in adjacent if i[1] >= 0]
    adjacent[:] = [i for i in adjacent if i[0] <= x_max]
    adjacent[:] = [i for i in adjacent if i[1] <= y_max]
    
    grid_tf = grid.copy()
    grid_tf.loc[:, :] = False
    for i in adjacent:
        grid_tf.loc[i] = True
    return grid_tf


def increment_grid(grid):
    grid += 1
    return grid


def flash_octopus(grid, flash_initial=0):
    flash_counter = 0
    if (grid > 9).sum().sum():
        flash_points = [(x, grid.columns[y]) for x, y in zip(*np.where(grid.values > 9))]
        grid[grid > 9] = 0
        for flash_point in flash_points:
            grid_adjacent = adjacent_points(grid, flash_point)
            grid[grid_adjacent & (grid != 0)] +=1
        grid, flashes = flash_octopus(grid)
        flash_counter += flashes
    else:
        flash_counter += grid[grid == 0].count().sum()
    return grid, flash_counter + flash_initial


def loop_steps(grid, steps):
    flashes = 0
    for i in range(steps):
        grid = increment_grid(grid)
        grid, flashes = flash_octopus(grid, flashes)
    return flashes


start_grid = read_file(r'./year_2021/input/11_dumbo_octopus.txt')
print(f'Part 1 answer: {loop_steps(start_grid.copy(), 100)}')


def all_flash(grid):
    synchronized = False
    steps = 0
    while not synchronized:
        steps += 1
        grid = increment_grid(grid)
        grid, _ = flash_octopus(grid, 0)
        synchronized = (grid.values == grid.loc[0,0]).all()
    return steps


print(f'Part 2 answer: {all_flash(start_grid.copy())}')