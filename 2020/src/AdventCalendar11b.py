import copy

input_file = open('day2.txt')
content = input_file.readlines()

ns = 0
ew = 0
waypoint = [10, 1]
for line in content:
    direction = line[0]
    q = int(line[1:])

    if direction == 'N':
        waypoint[1] += q
    elif direction == 'S':
        waypoint[1] -= q
    elif direction == 'E':
        waypoint[0] += q
    elif direction == 'W':
        waypoint[0] -= q
    elif direction == 'L':
        waypointb = copy.deepcopy(waypoint)
        if q == 90:
            waypoint[0] = -1 * waypointb[1]
            waypoint[1] = waypointb[0]
        if q == 180:
            waypoint[0] = -1 * waypointb[0]
            waypoint[1] = -1 * waypointb[1]
        if q == 270:
            waypoint[0] = waypointb[1]
            waypoint[1] = -1 * waypointb[0]
    elif direction == 'R':
        waypointb = copy.deepcopy(waypoint)
        if q == 90:
            waypoint[0] = waypointb[1]
            waypoint[1] = -1 * waypointb[0]
        if q == 180:
            waypoint[0] = -1 * waypointb[0]
            waypoint[1] = -1 * waypointb[1]
        if q == 270:
            waypoint[0] = -1 * waypointb[1]
            waypoint[1] = waypointb[0]
    elif direction == 'F':
        ns += waypoint[1] * q
        ew += waypoint[0] * q

print(abs(ns) + abs(ew))
