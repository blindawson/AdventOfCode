import numpy as np
import copy
import pickle

# ifn = r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input20example.txt'
# array_size = 3
ifn = r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input20.txt'
array_size = 12
tile_size = 10
input_file = open(ifn, 'r')
content = [i.strip() for i in input_file.readlines()[:]]


def read_tile(file, line):
    tile_id = int(file[line].split(' ')[-1][:-1])
    tile_data = np.empty((tile_size, tile_size), str)
    for i in range(tile_size):
        tile_data[i] = [x for x in file[line + 1 + i]]
    return tile_id, tile_data


def read_file(file):
    tile_ids = []
    tile_datas = []
    for line in range(0, len(file), tile_size+2):
        tile_id, tile_data = read_tile(file, line)
        tile_ids.append(tile_id)
        tile_datas.append(tile_data)
    return tile_ids, tile_datas


def advance_tile(x, y):
    x += 1
    if x == array_size:
        y += 1
        x = 0
    return x, y


def backup_tile(x, y):
    x -= 1
    if x == -1:
        y -= 1
        x = array_size - 1
    return x, y


def match_side(tile1, tile2, side):
    if side == 'top':
        if (tile1[0, :] == tile2[-1, :]).all():
            return True
    elif side == 'bottom':
        if (tile1[-1, :] == tile2[0, :]).all():
            return True
    elif side == 'right':
        if (tile1[:, -1] == tile2[:, 0]).all():
            return True
    elif side == 'left':
        if (tile1[:, 0] == tile2[:, -1]).all():
            return True
    else:
        return False


def choose_matches(row, col):
    sides = []
    if row != 0:
        sides.append('left')
    if row != array_size - 1:
        sides.append('right')
    if col != 0:
        sides.append('top')
    if col != array_size - 1:
        sides.append('bottom')


def rot_flip(m, i):
    if i <= 4:
        return np.rot90(m, i)
    elif i <= 8:
        return np.rot90(np.fliplr(m), i-4)
    else:
        raise ValueError('Roation must be 1-8')


def tile_fits(tile, tile_array, x, y):
    try:
        left_match = match_side(tile, tile_array[x - 1, y], 'left')
    except (TypeError, IndexError):
        left_match = True
    try:
        right_match = match_side(tile, tile_array[x + 1, y], 'right')
    except (TypeError, IndexError):
        right_match = True
    try:
        top_match = match_side(tile, tile_array[x, y + 1], 'top')
    except (TypeError, IndexError):
        top_match = True
    try:
        bottom_match = match_side(tile, tile_array[x, y - 1], 'bottom')
    except (TypeError, IndexError):
        bottom_match = True
    if left_match and right_match and top_match and bottom_match:
        return True
    else:
        return False


def fit_tile(ids, tiles, tile_array, used_tiles, x, y):
    finished = False
    for id_, tile in zip(ids, tiles):
        if id_ not in used_tiles:
            for r in range(1, 9):
                rot_tile = rot_flip(tile, r)
                if tile_fits(rot_tile, tile_array, x, y):
                    if (x == array_size - 1) and (y == array_size - 1):
                        tile_array[x, y] = rot_tile
                        used_tiles.append(id_)
                        finished = True
                    else:
                        new_array = copy.deepcopy(tile_array)
                        new_used_tiles = copy.deepcopy(used_tiles)
                        new_array[x, y] = rot_tile
                        new_used_tiles.append(id_)
                        new_x, new_y = advance_tile(x, y)
                        finished, new_tile_array, new_used_tiles = fit_tile(ids, tiles,
                                                                    new_array, new_used_tiles,
                                                                    new_x, new_y)
                        if finished:
                            tile_array = new_tile_array
                            used_tiles = new_used_tiles
    return finished, tile_array, used_tiles


if __name__ == "__main__":
    ids, tiles = read_file(content)
    tile_array = np.empty((array_size, array_size), np.ndarray)
    used_tiles = []
    corner_tiles = []

    finished, tile_array, used_tiles = fit_tile(ids, tiles, tile_array, used_tiles, 0, 0)
    used_tiles = np.reshape(used_tiles, (array_size, array_size))
    print(used_tiles)
    corner_tiles = np.array([used_tiles[0, 0],
                             used_tiles[array_size-1, 0],
                             used_tiles[0, array_size-1],
                             used_tiles[array_size-1, array_size-1]], dtype='int64')
    print(corner_tiles)
    print(np.prod(corner_tiles))

    filehandler = open('../output/aoc20_output.pkl', 'wb')
    pickle.dump(tile_array, filehandler)
