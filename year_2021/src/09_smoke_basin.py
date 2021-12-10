basin_file = open(r'../input/09_smoke_basin.txt')
# basin_file = open(r'../input/09_test_input.txt')
terrain = [list(x) for x in basin_file.read().splitlines()]
for d, depths in enumerate(terrain):
    terrain[d] = [int(x) for x in depths]
terrain_size = [len(terrain), len(terrain[0])]


def point_out_of_bounds(x, y):
    if (x < 0) | (x >= terrain_size[0]) | (y < 0) | (y >= terrain_size[1]):
        return True
    else:
        return False


def remove_out_of_bounds_coordinates(coordinates):
    bad_coordinates = []
    for coordinate in coordinates:
        if point_out_of_bounds(coordinate[0], coordinate[1]):
            bad_coordinates.append(coordinate)
    [coordinates.remove(c) for c in bad_coordinates]
    return coordinates


def find_nearby_coordinates(x, y):
    nearby_coordinates = [[x - 1, y],
                          [x, y - 1],
                          [x + 1, y],
                          [x, y + 1]]
    return remove_out_of_bounds_coordinates(nearby_coordinates)


def find_local_min(x, y):
    point = terrain[x][y]
    nearby_coordinates = find_nearby_coordinates(x, y)
    nearby_points = [terrain[i][j] for i, j in nearby_coordinates]
    for nearby_coordinate, nearby_point in zip(nearby_coordinates, nearby_points):
        if point >= nearby_point:
            return 0
    return point+1


risk_level_sum = 0
for x in range(terrain_size[0]):
    for y in range(terrain_size[1]):
        risk_level_sum += find_local_min(x, y)

print(f'Part 1 answer: {risk_level_sum}')


def remove_9_points(coordinates, points):
    bad_coordinates = []
    bad_points = []
    for coordinate, point in zip(coordinates, points):
        if point == 9:
            bad_coordinates.append(coordinate)
            bad_points.append(point)
    [coordinates.remove(c) for c in bad_coordinates]
    [points.remove(c) for c in bad_points]
    return coordinates, points


def higher_adjacent_points(x, y):
    higher_points = []
    point = terrain[x][y]
    nearby_coordinates = find_nearby_coordinates(x, y)
    nearby_points = [terrain[i][j] for i, j in nearby_coordinates]
    nearby_coordinates, nearby_points = remove_9_points(nearby_coordinates, nearby_points)
    for nearby_coordinate, nearby_point in zip(nearby_coordinates, nearby_points):
        if nearby_point > point:
            if nearby_point not in higher_points:
                higher_points.append(nearby_coordinate)
            [higher_points.append(x)
             for x in higher_adjacent_points(nearby_coordinate[0], nearby_coordinate[1])
             if x not in higher_points]

    return higher_points


higher_adjacent_points(2,2)
basin_sizes = []
for x in range(terrain_size[0]):
    for y in range(terrain_size[1]):
        if find_local_min(x, y):
            basin_size = 1
            basin_size += len(higher_adjacent_points(x, y))
            basin_sizes.append(basin_size)

basin_sizes.sort(reverse=True)

print(basin_sizes[:3])
print(f'Part 2 answer: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}')
