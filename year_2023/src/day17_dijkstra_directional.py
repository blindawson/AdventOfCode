from AdventOfCode.support import support
import numpy as np
import copy
import itertools


class Crucible:
    def __init__(self, filename, part2=False):
        self.heat_grid = np.array(support.read_input(filename, flavor="int_grid"))
        self.part2 = part2
        if self.part2:
            self.line_range = (4, 10)
        else:
            self.line_range = (1, 3)

        self.keys = [
            str(x[0]) + x[1]
            for x in list(
                itertools.product(
                    range(self.line_range[0], self.line_range[1] + 1),
                    ["N", "S", "E", "W"],
                )
            )
        ]

        self.empty_dict = {}
        for key in self.keys:
            self.empty_dict[key] = np.nan
        self.heat_dicts = np.empty(self.heat_grid.shape, dtype=dict)
        # Fill in each element with a copy of the dictionary
        for i in range(self.heat_grid.shape[0]):
            for j in range(self.heat_grid.shape[1]):
                self.heat_dicts[i, j] = copy.deepcopy(self.empty_dict)
        self.staging_dicts = copy.deepcopy(self.heat_dicts)
        self.staging_ints = np.full(self.heat_grid.shape, np.nan)

        self.active_nodes = np.zeros(self.heat_grid.shape, dtype=bool)
        self.pos = (0, 0)
        self.active_nodes[self.pos] = True
        self.heat_dicts[self.pos][str(self.line_range[1]) + "E"] = 1
        self.heat_dicts[self.pos][str(self.line_range[1]) + "S"] = 1
        start_num_str = str(self.line_range[0])
        self.turn_dir_dict = {
            "N": [start_num_str + "E", start_num_str + "W"],
            "S": [start_num_str + "E", start_num_str + "W"],
            "W": [start_num_str + "S", start_num_str + "N"],
            "E": [start_num_str + "N", start_num_str + "S"],
        }

        self.empty_map_dict = {}
        for key in self.keys:
            self.empty_map_dict[key] = []

    def is_point_in_grid(self, node):
        return not support.point_out_of_bounds(node[0], node[1], self.heat_dicts)

    def adjacent_nodes(self, active_node, dist):
        return {
            "E": (active_node[0], active_node[1] + dist),
            "W": (active_node[0], active_node[1] - dist),
            "S": (active_node[0] + dist, active_node[1]),
            "N": (active_node[0] - dist, active_node[1]),
        }

    # Give a dictionary showing each key in active node and which empty adjacent keys it connects to
    def dict_to_dict_mapping(self, active_node):
        map_dict = copy.deepcopy(self.empty_map_dict)

        for move_dir in self.adjacent_nodes(active_node, self.line_range[0]).keys():
            node_in_that_direction = self.adjacent_nodes(
                active_node, self.line_range[0]
            )[move_dir]
            turn_node_strs = self.turn_dir_dict[move_dir]

            # For all key values check the adjacent turn 1 values
            for key in [x for x in self.keys if x[-1] == move_dir]:
                # If we're above the min threshold for moving in straight line
                if int(key[:-1]) >= self.line_range[0]:
                    # If we have a value for 1N (or 2E, 3W, etc.)
                    if not np.isnan(self.heat_dicts[active_node][key]):
                        # For nodes to east and west
                        for turn_node_str in turn_node_strs:
                            node = self.adjacent_nodes(active_node, self.line_range[0])[
                                turn_node_str[-1]
                            ]
                            # If east_node[1E] or west_node[1W] exists and is blank
                            if (
                                self.is_point_in_grid(node)
                                and np.isnan(self.heat_dicts[node][turn_node_str])
                                and (self.staging_dicts[node][turn_node_str] != np.inf)
                            ):
                                map_dict[key].append((node, turn_node_str))

            node_in_that_direction = self.adjacent_nodes(
                active_node, 1
            )[move_dir]
            for i in range(self.line_range[0], self.line_range[1]):
                key = str(i) + move_dir
                key1 = str(i + 1) + move_dir
                # If we have a value for 1N
                if not np.isnan(self.heat_dicts[active_node][key]):
                    # If north_node[2N] is blank
                    if (
                        self.is_point_in_grid(node_in_that_direction)
                        and np.isnan(self.heat_dicts[node_in_that_direction][key1])
                        and (self.staging_dicts[node_in_that_direction][key1] != np.inf)
                    ):
                        map_dict[key].append((node_in_that_direction, key1))
        return map_dict

    def update_active_nodes(self, node):
        if any(list(self.dict_to_dict_mapping(node).values())):
            self.active_nodes[node] = True
        else:
            self.active_nodes[node] = False

    def cost(self, new_node, new_key):
        if new_key[-1] == "E":
            rows = [new_node[0]]
            cols = range(self.pos[1] + 1, new_node[1] + 1)
        elif new_key[-1] == "W":
            rows = [new_node[0]]
            cols = range(new_node[1], self.pos[1])
        elif new_key[-1] == "S":
            rows = range(self.pos[0] + 1, new_node[0] + 1)
            cols = [new_node[1]]
        elif new_key[-1] == "N":
            rows = range(new_node[0], self.pos[0])
            cols = [new_node[1]]
        sum_cost = 0
        for row, col in list(itertools.product(rows, cols)):
            node = (row, col)
            sum_cost += self.heat_grid[node]
        return sum_cost

    def update_staging(self):
        map_dict = self.dict_to_dict_mapping(self.pos)
        for active_key, new_values in map_dict.items():
            if new_values:
                for new_value in new_values:
                    new_node = new_value[0]
                    new_key = new_value[1]
                    new_len = self.heat_dicts[self.pos][active_key] + self.cost(
                        new_node, new_key
                    )
                    if (new_len < self.staging_dicts[new_node][new_key]) or np.isnan(
                        self.staging_dicts[new_node][new_key]
                    ):
                        self.staging_dicts[new_node][new_key] = new_len
                        self.staging_ints[new_node] = np.nanmin(
                            [self.staging_ints[new_node], new_len]
                        )

    def dijkstra(self):
        while not any([not np.isnan(x) for x in self.heat_dicts[(-1, -1)].values()]):
            print(self.pos)
            self.update_staging()
            min_len = np.nanmin(self.staging_ints)
            min_node = np.where(self.staging_ints == min_len)
            min_node = (min_node[0][0], min_node[1][0])
            for key, value in self.staging_dicts[min_node].items():
                if value == min_len:
                    min_key = key
            self.heat_dicts[min_node][min_key] = min_len
            self.pos = min_node
            self.staging_dicts[min_node][min_key] = np.inf
            self.staging_ints[min_node] = np.nanmin(
                list(self.staging_dicts[min_node].values())
            )

    def min_heat_loss(self):
        self.dijkstra()
        return [x for x in self.heat_dicts[-1, -1].values() if not np.isnan(x)][0] - 1


filename = r"year_2023/tests/test_inputs/17_test_input.txt"
# m = Crucible(filename, part2=False)
m = Crucible(filename, part2=True)
m.min_heat_loss()
m.dict_to_dict_mapping((0, 4))
