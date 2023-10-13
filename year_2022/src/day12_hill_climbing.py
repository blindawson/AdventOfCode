import numpy as np
from puzzle_init import *

class Node()


def dijkstra_algorithm(grid):
    # Figure out which node to evaluate next
    def find_current_node():
        if (prelim_total_cost == np.zeros(grid_size)).all():
            # Find start node
            for ix, row in enumerate(grid):
                for iy, i in enumerate(row):
                    if i == "S":
                        grid[ix, iy] = "a"
                        return ix, iy
        else:
            # Find the node with the lowest total cost
            min_cost = np.min(prelim_total_cost[np.nonzero(prelim_total_cost)])
            min_cost_locs = np.where(prelim_total_cost == min_cost)
            return min_cost_locs[0][0], min_cost_locs[1][0]

    def update_prelim_cost(current_node):
        # print(current_node)
        current_cost = prelim_total_cost[current_node]
        for adjacent in adjacent_coordinates[current_node]:
            adj_x, adj_y = adjacent
            if visited[adj_x, adj_y] == 0:
                if prelim_total_cost[adj_x, adj_y] == 0:
                    prelim_total_cost[adj_x, adj_y] = current_cost + 1
                else:
                    prelim_total_cost[adj_x, adj_y] = min(
                        prelim_total_cost[adj_x, adj_y], current_cost + 1
                    )

    def set_final_total_cost(current_node):
        final_total_cost[current_node] = prelim_total_cost[current_node]
        visited[current_node] = 1
        prelim_total_cost[current_node] = 0

    def remove_out_of_reach_coordinates(current_node, nearby_coordinates, grid):
        current_node_val = ord(grid[current_node[0]][current_node[1]])
        bad_coordinates = []
        for coordinate in nearby_coordinates:
            coordinate_val = ord(grid[coordinate[0]][coordinate[1]])
            if coordinate_val - current_node_val > 1:
                bad_coordinates.append(coordinate)
        [nearby_coordinates.remove(c) for c in bad_coordinates]
        return nearby_coordinates

    def find_nearby_reachable_coordinates(grid):
        nearby_coordinates = np.zeros([len(grid), len(grid[0])], dtype=np.ndarray)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                nearby_prelim_list = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
                nearby_prelim_list = support.remove_out_of_bounds_coordinates(
                    nearby_prelim_list, grid
                )
                nearby_coordinates[x, y] = remove_out_of_reach_coordinates(
                    [x, y], nearby_prelim_list, grid
                )
        return nearby_coordinates

    def find_end_node(grid):
        end_node = [
            (ix, iy)
            for ix, row in enumerate(grid)
            for iy, i in enumerate(row)
            if i == "E"
        ][0]
        grid[end_node[0]][end_node[1]] = "z"
        return end_node

    grid_size = [len(grid), len(grid[0])]
    adjacent_coordinates = find_nearby_reachable_coordinates(grid)
    prelim_total_cost = np.zeros(grid_size)
    final_total_cost = np.zeros(grid_size)
    visited = np.zeros(grid_size)

    current_node = find_current_node()
    end_node = find_end_node(grid)
    adjacent_coordinates = find_nearby_reachable_coordinates(grid)
    hill_map[current_node] = "S"

    i = 0
    while final_total_cost[end_node] == 0:
        # print(i)
        i += 1
        current_node = find_current_node()
        update_prelim_cost(current_node)
        set_final_total_cost(current_node)
    return int(final_total_cost[end_node])


# hill_map = support.read_input(
#     r"year_2022/tests/12_hill_climbing.txt", flavor="str_grid"
# )
# hill_map = np.array([np.array(xi) for xi in hill_map])
# print(f"Part 1 answer: {dijkstra_algorithm(hill_map)}")

hill_map = support.read_input(
    r"year_2022/input/12_hill_climbing.txt", flavor="str_grid"
)
hill_map = np.array([np.array(xi) for xi in hill_map])
print(f"Part 1 answer: {dijkstra_algorithm(hill_map)}")
