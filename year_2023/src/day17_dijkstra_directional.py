from AdventOfCode.support import support
import numpy as np
import copy
import itertools


class Crucible:
    def __init__(self, filename, part2=False):
        self.heat_grid = np.array(support.read_input(filename, flavor="int_grid"))
        self.part2 = part2
        if self.part2:
            self.straight_line_max = 10
            self.line_min = 4
        else:
            self.straight_line_max = 3
            self.line_min = 1

        self.keys = [
            str(x[0]) + x[1]
            for x in list(
                itertools.product(
                    range(1, self.straight_line_max + 1), ["N", "S", "E", "W"]
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
        self.heat_dicts[self.pos][str(self.straight_line_max) + "E"] = 1
        self.heat_dicts[self.pos][str(self.straight_line_max) + "S"] = 1
        self.turn_dir_dict = {
            "N": ["1E", "1W"],
            "S": ["1E", "1W"],
            "W": ["1S", "1N"],
            "E": ["1N", "1S"],
        }

        self.empty_map_dict = {}
        for key in self.keys:
            self.empty_map_dict[key] = []

    def is_point_in_grid(self, node):
        return not support.point_out_of_bounds(node[0], node[1], self.heat_dicts)

    # Give a dictionary showing each key in active node and which empty adjacent keys it connects to
    def dict_to_dict_mapping(self, active_node):
        map_dict = copy.deepcopy(self.empty_map_dict)

        adjacent_nodes = {
            "E": (active_node[0], active_node[1] + 1),
            "W": (active_node[0], active_node[1] - 1),
            "S": (active_node[0] + 1, active_node[1]),
            "N": (active_node[0] - 1, active_node[1]),
        }
        for move_dir in adjacent_nodes.keys():
            node_in_that_direction = adjacent_nodes[move_dir]
            turn_node_strs = self.turn_dir_dict[move_dir]

            # For all key values check the adjacent turn 1 values
            for key in [x for x in self.keys if x[-1] == move_dir]:
                # If we're above the min threshold for moving in straight line
                if int(key[:-1]) >= self.line_min:
                    # If we have a value for 1N (or 2E, 3W, etc.)
                    if not np.isnan(self.heat_dicts[active_node][key]):
                        # For nodes to east and west
                        for turn_node_str in turn_node_strs:
                            node = adjacent_nodes[turn_node_str[-1]]
                            # If east_node[1E] or west_node[1W] exists and is blank
                            if (
                                self.is_point_in_grid(node)
                                and np.isnan(self.heat_dicts[node][turn_node_str])
                                and (self.staging_dicts[node][turn_node_str] != np.inf)
                            ):
                                map_dict[key].append((node, turn_node_str))

            for i in range(1, self.straight_line_max):
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

    def update_staging(self):
        map_dict = self.dict_to_dict_mapping(self.pos)
        for active_key, new_values in map_dict.items():
            if new_values:
                for new_value in new_values:
                    new_node = new_value[0]
                    new_key = new_value[1]
                    new_len = (
                        self.heat_dicts[self.pos][active_key] + self.heat_grid[new_node]
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
            self.staging_ints[min_node] = np.nanmin(list(self.staging_dicts[min_node].values()))

    def min_heat_loss(self):
        self.dijkstra()
        return [x for x in self.heat_dicts[-1, -1].values() if not np.isnan(x)][0] - 1


filename = r"year_2023/tests/test_inputs/17_test_input.txt"
# m = Crucible(filename, part2=False)
m = Crucible(filename, part2=True)
m.min_heat_loss()
