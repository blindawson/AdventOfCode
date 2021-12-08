import numpy as np

input_file = open(r'..\input\03 wire paths.txt')
content = input_file.read().splitlines()
line_directions1 = content[0].split(',')
line_directions2 = content[1].split(',')


def read_direction_code(direction_code):
    direction = direction_code[0]
    distance = int(direction_code[1:])
    return direction, distance


def read_line_directions(line_directions):
    points_on_line = [(0, 0)]
    for direction_code in line_directions:
        direction, distance = read_direction_code(direction_code)
        for d in range(distance):
            if direction == 'U':
                new_point = (points_on_line[-1][0], points_on_line[-1][1] + 1)
            if direction == 'D':
                new_point = (points_on_line[-1][0], points_on_line[-1][1] - 1)
            if direction == 'R':
                new_point = (points_on_line[-1][0] + 1, points_on_line[-1][1])
            if direction == 'L':
                new_point = (points_on_line[-1][0] - 1, points_on_line[-1][1])
            points_on_line.append(new_point)
    points_on_line.pop(0)
    return points_on_line


def calculate_manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def calculate_steps(points_list, point):
    return points_list.index(point) + 1


points1 = read_line_directions(line_directions1)
points2 = read_line_directions(line_directions2)
intersections = list(set(points1) & set(points2))

intersection_distances = [calculate_manhattan_distance(intersection) for intersection in intersections]
print(min(intersection_distances))

intersection_steps1 = [calculate_steps(points1, intersection) for intersection in intersections]
intersection_steps2 = [calculate_steps(points2, intersection) for intersection in intersections]
intersection_steps_total = np.add(intersection_steps1, intersection_steps2)
print(min(intersection_steps_total))