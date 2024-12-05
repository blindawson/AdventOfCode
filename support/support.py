import numpy as np


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
    day = str(day).zfill(2)
    input_filename = f"year_{year}/input/{day}_{name}.txt"
    open(input_filename, "x")

    test_input_filename = f"year_{year}/tests/test_inputs/{day}_test_input.txt"
    open(test_input_filename, "x")

    src_filename = f"year_{year}/src/day{day}_{name}.py"
    src_file = open(src_filename, "w")
    src_file.write(
        "from support import support\n\n\n"
        + "class ClassName:\n"
        + "    def __init__(self, filename):\n"
        + "        self.file_input = support.read_input(filename, flavor=None, split_char=None)\n\n"
        + "    def part1(self):\n"
        + "        pass\n\n"
        + "    def part2(self):\n"
        + "        pass\n\n\n"
        + f'filename = r"{test_input_filename}"\n'
        + f'# filename = r"{input_filename}"\n'
        + "m = ClassName(filename)\n"
        + "m.file_input"
    )
    src_file.close()

    test_filename = f"year_{year}/tests/test_day{day}_{name}.py"
    test_file = open(test_filename, "w")
    test_file.write(
        f"from year_{year}.src import day{day}_{name} as d{day}\n\n\n"
        + "def test_example():\n"
        + f'    filename = r"{test_input_filename}"\n'
        + f"    m = d{day}.ClassName(filename)\n"
        + f"    assert m.part1() == 99\n\n\n"
        + "def test_part1():\n"
        + f'    filename = r"{input_filename}"\n'
        + f"    m = d{day}.ClassName(filename)\n"
        + f"    assert m.part1() == 99\n\n\n"
        + "def test_example_part2():\n"
        + f'    filename = r"{test_input_filename}"\n'
        + f"    m = d{day}.ClassName(filename)\n"
        + f"    assert m.part2() == 99\n\n\n"
        + "def test_part2():\n"
        + f'    filename = r"{input_filename}"\n'
        + f"    m = d{day}.ClassName(filename)\n"
        + f"    assert m.part2() == 99\n"
    )
    test_file.close()


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
            nearby_initial = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
            nearby_coordinates[x, y] = remove_out_of_bounds_coordinates(
                nearby_initial, grid
            )
    return nearby_coordinates


def list_neighbors(loc: tuple, grid, diagonal=False):
    # List coordinates adjacent to loc
    y, x = loc
    if diagonal:
        nearby_initial = [
            (y - 1, x),
            (y, x - 1),
            (y + 1, x),
            (y, x + 1),
            (y + 1, x + 1),
            (y + 1, x - 1),
            (y - 1, x + 1),
            (y - 1, x - 1),
        ]
    else:
        nearby_initial = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
    nearby_initial = remove_out_of_bounds_coordinates(nearby_initial, grid)
    return nearby_initial


def hex_to_bin(hex, scale=16, num_bits=4):
    return bin(int(hex, scale))[2:].zfill(num_bits * len(hex))


def bin_to_dec(bin_input):
    return int(bin_input, 2)


def list_ordinal_adjacent(pos: tuple[int]):
    return [
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
    ]


def list_all_adjacent(pos: tuple[int]):
    return [
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0] - 1, pos[1] - 1),
        (pos[0] + 1, pos[1] - 1),
        (pos[0] + 1, pos[1] + 1),
        (pos[0] - 1, pos[1] + 1),
    ]


# Split a range depending on how it overlaps with another range
def split_range(range1: tuple, range2: tuple):
    # If range1 within range2
    if (range1[0] >= range2[0]) and (range1[1] <= range2[1]):
        # return range 1
        return [range1]
    # If range2 within range1
    elif (range1[0] < range2[0]) and (range1[1] > range2[1]):
        # Split range 1 into 3 ranges
        return [
            (range1[0], range2[0] - 1),
            (range2[0], range2[1]),
            (range2[1] + 1, range1[1]),
        ]
    # If new range overlaps with existing range
    elif (range1[0] >= range2[0]) and (range1[0] <= range2[1]):
        # Split range 1 into 2 ranges
        return [(range1[0], range2[1]), (range2[1] + 1, range1[1])]
    # If new range overlaps with existing range
    elif (range2[0] >= range1[0]) and (range2[0] <= range1[1]):
        # Split range 1 into 2 ranges
        return [(range1[0], range2[0] - 1), (range2[0], range1[1])]
    else:
        return [range1]


direction_dict = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}


def sum_tuples(tuple1, tuple2):
    return tuple(x + y for x, y in zip(tuple1, tuple2))


def subtract_tuples(tuple1, tuple2):
    return tuple(x - y for x, y in zip(tuple1, tuple2))


def reverse_array(a):
    return a[::-1]
