import numpy as np
from typing import Union


def create_files(year: int, day: int, name: str):
    """Create the input, src, and test files you need for
    another day of Advent of Code

    Parameters
    ----------
    year : int
        The year of the puzzle.
    day : int
        The day of the puzzle.
    name : str
        The name of the puzzle.
    """
    input_filename = f"year_{year}/input/{day}_{name}.txt"
    open(input_filename, "x")

    src_filename = f"year_{year}/src/day{day}_{name}.py"
    src_file = open(src_filename, "w")
    src_file.write(
        "from AdventOfCode.support import support\n\n\n"
        + "class ClassName:\n"
        + "    def __init__(self, filename):\n"
        + "        self.file_input = support.read_input(\n"
        + "filename, flavor=None, split_char=None)\n"
    )
    src_file.close()

    test_filename = f"year_{year}/tests/test_day{day}_{name}.py"
    test_file = open(test_filename, "w")
    test_file.write(
        f"from AdventOfCode.year_{year}.src import day{day}_{name} as d{day}\n\n\n"
        + "def test_example():\n"
        + f"    filename = r'year_{year}/tests/test_inputs/{day}_test_input.txt'\n"
        + f"    assert d{day}.ClassName(filename) == 99\n\n\n"
        + "def test_part1():\n"
        + f"    filename = r'year_{year}/input/{day}_{name}.txt'\n"
        + f"    assert d{day}.ClassName(filename) == 99\n\n\n"
        + "def test_example_part2():\n"
        + f"    filename = r'year_{year}/tests/test_inputs/{day}_test_input.txt'\n"
        + f"    assert d{day}.ClassName(filename) == 99\n\n\n"
        + "def test_part2():\n"
        + f"    filename = r'year_{year}/input/{day}_{name}.txt'\n"
        + f"    assert d{day}.ClassName(filename) == 99\n"
    )
    test_file.close()

    test_input_filename = f"year_{year}/tests/test_inputs/{day}_test_input.txt"
    open(test_input_filename, "x")


def read_input(filename, flavor=None, split_char=None):
    open_file = open(filename).read().splitlines()
    if flavor == "split":
        open_file = [x.split(split_char) for x in open_file]
    elif flavor == "split_int":
        open_file = [tuple(map(int, x.split(split_char))) for x in open_file]
    elif flavor == "int_grid":
        open_file = [list(map(int, x)) for x in open_file]
    elif flavor == "str_grid":
        open_file = [list(map(str, x)) for x in open_file]
    return open_file


# Listing adjacent coordinates in a grid
def point_out_of_bounds(y: int, x: int, grid: list[list[int]]) -> bool:
    if (y < 0) | (y >= len(grid)) | (x < 0) | (x >= len(grid[0])):
        return True
    else:
        return False


def point_out_of_bounds_3D(x: int, y: int, z: int, grid: np.array) -> bool:
    if (
        (x < 0)
        | (x >= grid.shape[0])
        | (y < 0)
        | (y >= grid.shape[1])
        | (z < 0)
        | (z >= grid.shape[2])
    ):
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
            nearby_initial = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
            nearby_coordinates[x, y] = remove_out_of_bounds_coordinates(
                nearby_initial, grid
            )
    return nearby_coordinates


def hex_to_bin(hex, scale=16, num_bits=4):
    return bin(int(hex, scale))[2:].zfill(num_bits * len(hex))


def bin_to_dec(bin_input):
    return int(bin_input, 2)
