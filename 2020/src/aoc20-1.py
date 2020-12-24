import numpy as np

ifn = r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input20.txt'
input_file = open(ifn, 'r')
content = [i.strip() for i in input_file.readlines()[:]]


def read_tile(line):
    tile_id = int(content[line].split(' ')[-1][:-1])
    tile_data = np.empty((10, 10), str)
    for i in range(10):
        tile_data[i] = [x for x in content[line + 1 + i]]
    return tile_id, tile_data


def read_file():
    tile_ids = []
    tile_datas = []
    for line in range(0, 1728, 12):
        tile_id, tile_data = read_tile(line)
        tile_ids.append(tile_id)
        tile_datas.append(tile_data)
    return tile_ids, tile_datas


def match_side(tile1, tile2, side):
    if side == 'top':
        if tile1[0, :] == tile2[-1, :]:
            return True
    elif side == 'bottom':
        if tile1[-1, :] == tile2[0, :]:
            return True
    elif side == 'right':
        if tile1[:, -1] == tile2[:, 0]:
            return True
    elif side == 'left':
        if tile1[:, 0] == tile2[:, -1]:
            return True
    else:
        return False


def choose_matches(row, col):
    sides = []
    if row != 0:
        sides.append('left')
    if row != 11:
        sides.append('right')
    if col != 0:
        sides.append('top')
    if col != 11:
        sides.append('bottom')


if __name__ == "__main__":
    ids, tiles = read_file()
    tile_array = np.empty((12, 12), np.ndarray)
    used_tiles = []
    corner_tiles = []

    # for each column
    for x in range(12):
        # for each row
        for y in range(12):
            # for each tile
            for id_, tile in zip(ids, tiles):
                # todo for all rotations and flipes of tile:
                    if id_ not in used_tiles:
                        try:
                            left_match = match_side(tile, tile_array[x-1, y], 'left')
                        except TypeError:
                            left_match = True
                        try:
                            right_match = match_side(tile, tile_array[x+1, y], 'right')
                        except TypeError:
                            right_match = True
                        try:
                            top_match = match_side(tile, tile_array[x, y+1], 'top')
                        except TypeError:
                            top_match = True
                        try:
                            bottom_match = match_side(tile, tile_array[x, y-1], 'bottom')
                        except TypeError:
                            bottom_match = True
                        if left_match and right_match and top_match and bottom_match:
                            tile_array[x, y] = tile
                            used_tiles.append(id_)
                            break
            # todo if none of the next tiles fit then go back a tile, continue trying flips/rotates of previous
            # todo and if none of the flips/rotates of that previous tile work then continue trying other tiles

    print(np.prod(corner_tiles))

