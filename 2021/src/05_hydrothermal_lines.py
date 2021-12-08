import re
import numpy as np

lines_file = open(r'../input/05_hydrothermal_lines.txt')
lines_list = np.array([re.split(' -> |,', x) for x in lines_file.read().splitlines()]).astype(int)


def horizontal_or_vertical_line(coordinates):
    [x1, y1, x2, y2] = coordinates
    if (x1 == x2) or (y1 == y2):
        return True
    else:
        return False


def line_direction(coordinates):
    [x1, y1, x2, y2] = coordinates
    if x2 > x1:
        x_direction = 1
    else:
        x_direction = -1
    if y2 > y1:
        y_direction = 1
    else:
        y_direction = -1
    return x_direction, y_direction


line_count = np.zeros([lines_list.max()+1, lines_list.max()+1])
for line in lines_list:
    if horizontal_or_vertical_line(line):
        [x1, y1, x2, y2] = line
        for x in range(min([x1, x2]), max([x1, x2])+1):
            for y in range(min([y1, y2]), max([y1, y2])+1):
                line_count[x, y] += 1

print(f'Part 1 answer: {(line_count >= 2).sum()}')

for line in lines_list:
    if not horizontal_or_vertical_line(line):
        [x1, y1, x2, y2] = line
        [x_direction, y_direction] = line_direction(line)
        for (x, y) in zip(range(x1, x2+x_direction, x_direction), range(y1, y2+y_direction, y_direction)):
            line_count[x, y] += 1

print(f'Part 2 answer: {(line_count >= 2).sum()}')
