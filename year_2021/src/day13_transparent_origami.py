# %%

from AdventOfCode.support import support
import matplotlib.pyplot as plt

point_file = support.read_input(
    r"year_2021/input/13_transparent_origami_points.txt",
    flavor="split_int",
    split_char=",",
)
fold_file = support.read_input(
    r"year_2021/input/13_transparent_origami_folds.txt", flavor="split", split_char="="
)
for i, instruction in enumerate(fold_file):
    fold_file[i][0] = instruction[0][-1]
    fold_file[i][1] = int(instruction[1])


def fold_coordinate(coordinate, fold_position):
    coordinate_diff = coordinate - fold_position
    if coordinate_diff > 0:
        return coordinate - 2 * coordinate_diff
    else:
        return coordinate


def fold_page(fold_direction, fold_position, point_list):
    if fold_direction == "x":
        point_list = [(fold_coordinate(x[0], fold_position), x[1]) for x in point_list]
    if fold_direction == "y":
        point_list = [(x[0], fold_coordinate(x[1], fold_position)) for x in point_list]
    return point_list


def count_points(point_list):
    return len(set(point_list))


folded = fold_page(fold_file[0][0], fold_file[0][1], point_file)
print(f"Part 1 answer: {count_points(folded)}")

for fold in fold_file:
    point_file = fold_page(fold[0], fold[1], point_file)

x = [i[0] for i in point_file]
y = [i[1] * -1 for i in point_file]
plt.scatter(x, y)
# %%
