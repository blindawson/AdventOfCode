import numpy as np


def create_files(year, day, name):
    input_file = f'{year}/input/{day}_{name}.txt'
    src_file = f'{year}/src/day{day}_{name}.py'
    test_file = f'{year}/tests/test_day{day}_{name}.py'
    test_input_file = f'{year}/tests/test_inputs/{day}_test_input.txt'
    i = open(input_file, 'x')
    s = open(src_file, 'x')
    t = open(test_file, 'x')
    ti = open(test_input_file, 'x')


def read_input(filename, flavor=None, split_char=None):
    open_file = open(filename).read().splitlines()
    if flavor == 'split':
        open_file = [x.split(split_char) for x in open_file]
    elif flavor == 'split_int':
        open_file = [tuple(map(int, x.split(split_char))) for x in open_file]
    elif flavor == 'int_grid':
        open_file = [list(map(int, x)) for x in open_file]
    return open_file
    
    
# Listing adjacent coordinates in a grid
def point_out_of_bounds(x, y, grid):
    if (x < 0) | (x >= len(grid)) | (y < 0) | (y >= len(grid[0])):
        return True
    else:
        return False


def remove_out_of_bounds_coordinates(coordinates, grid):
    bad_coordinates = []
    for coordinate in coordinates:
        if point_out_of_bounds(coordinate[0], coordinate[1], grid):
            bad_coordinates.append(coordinate)
    [coordinates.remove(c) for c in bad_coordinates]
    return coordinates


def find_nearby_coordinates(grid):
    nearby_coordinates = np.zeros([len(grid), len(grid[0])], dtype=np.ndarray)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            nearby_initial = [[x - 1, y],
                              [x, y - 1],
                              [x + 1, y],
                              [x, y + 1]]
            nearby_coordinates[x, y] = remove_out_of_bounds_coordinates(nearby_initial, grid)
    return nearby_coordinates
    

def hex_to_bin(hex, scale=16, num_bits=4):
    return bin(int(hex, scale))[2:].zfill(num_bits*len(hex))


def bin_to_dec(bin_input):
    return int(bin_input, 2)