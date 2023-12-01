import numpy as np
import copy

input_file = open(r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input17.txt', 'r')
content = input_file.readlines()
content_rows = len(content)
content_cols = len(content[-1])

cycles = 6
grid = np.chararray((cycles * 2 + 1, cycles * 2 + content_rows, cycles * 2 + content_cols))
grid[:] = b'.'

for i, row in enumerate(content):
    row = list(row)
    try:
        row.remove('\n')
    except ValueError:
        pass
    for j, val in enumerate(row):
        grid[cycles][cycles + i][cycles + j] = val

grid1 = copy.deepcopy(grid)

for time in range(cycles):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for z in range(len(grid[0][0])):
                near = []
                middle_val = grid[x][y][z]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        for k in range(-1, 2):
                            try:
                                near_val = grid[x+i][y+j][z+k]
                            except IndexError:
                                continue
                            if (i == 0) and (j == 0) and (k == 0):
                                pass
                            else:
                                near.append(near_val)

                if middle_val == b'#':
                    if near.count(b'#') in [2, 3]:
                        grid1[x][y][z] = b'#'
                    else:
                        grid1[x][y][z] = b'.'
                elif middle_val == b'.':
                    if near.count(b'#') == 3:
                        grid1[x][y][z] = b'#'
                    else:
                        grid1[x][y][z] = b'.'
                else:
                    raise ValueError('Value not . or #')
    grid = copy.deepcopy(grid1)
print(grid)

active = 0
for x in grid:
    # print(x)
    for y in x:
        active += y.count(b'#')
        print(y.count(b'#'))
print(sum(active))


