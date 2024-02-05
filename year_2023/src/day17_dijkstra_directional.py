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
        else:
            self.straight_line_max = 3

        self.keys = [
            str(x[0]) + x[1]
            for x in list(
                itertools.product(
                    range(1, self.straight_line_max + 1), ["N", "S", "E", "W"]
                )
            )
        ]
        
        self.empty_dict = {}
        for combo in self.keys:
            self.empty_dict[combo] = np.nan
        self.empty_grid = np.empty(self.heat_grid.shape, dtype=dict)
        # Fill in each element with a copy of the dictionary
        for i in range(self.heat_grid.shape[0]):
            for j in range(self.heat_grid.shape[1]):
                self.empty_grid[i, j] = copy.deepcopy(self.empty_dict)
        self.heat_dicts = copy.deepcopy(self.empty_grid)
        self.staging_dicts = {}

        self.active_nodes = np.zeros(self.heat_grid.shape, dtype=bool)
        self.pos = (0, 0)
        self.active_nodes[self.pos] = True
        self.heat_dicts[self.pos]["3E"] = 1
        self.heat_dicts[self.pos]["3S"] = 1
        self.reverse_dir_dict = {"N": "S", "S": "N", "E": "W", "W": "E"}
        self.turn_dir_dict = {
            "N": ["1E", "1W"],
            "S": ["1E", "1W"],
            "W": ["1S", "1N"],
            "E": ["1N", "1S"],
        }

    def create_empty_dict(self):
        array = np.empty(self.heat_grid.shape, dtype=dict)
        # Fill in each element with a copy of the dictionary
        for i in range(self.heat_grid.shape[0]):
            for j in range(self.heat_grid.shape[1]):
                array[i, j] = copy.deepcopy(self.empty_dict)
        return array

    def is_point_in_grid(self, node):
        return not support.point_out_of_bounds(node[0], node[1], self.heat_dicts)

    # Give a dictionary showing each key in active node and which empty adjacent keys it connects to
    def dict_to_dict_mapping(self, active_node):
        map_dict = {
            "1N": [],
            "2N": [],
            "3N": [],
            "1E": [],
            "2E": [],
            "3E": [],
            "1S": [],
            "2S": [],
            "3S": [],
            "1W": [],
            "2W": [],
            "3W": [],
        }
        adjacent_nodes = {
            "E": (active_node[0], active_node[1] + 1),
            "W": (active_node[0], active_node[1] - 1),
            "S": (active_node[0] + 1, active_node[1]),
            "N": (active_node[0] - 1, active_node[1]),
        }
        for move_dir in adjacent_nodes.keys():
            one_dir = "1" + move_dir
            two_dir = "2" + move_dir
            three_dir = "3" + move_dir
            node_in_that_direction = adjacent_nodes[move_dir]
            turn_node_strs = self.turn_dir_dict[move_dir]

            # For all key values check the adjacent turn 1 values
            for ndir in [one_dir, two_dir, three_dir]:
                # If we have a value for 1N (or 2E, 3W, etc.)
                if not np.isnan(self.heat_dicts[active_node][ndir]):
                    # For nodes to east and west
                    for turn_node_str in turn_node_strs:
                        node = adjacent_nodes[turn_node_str[-1]]
                        # If east_node[1E] or west_node[1W] exists and is blank
                        if self.is_point_in_grid(node) and np.isnan(
                            self.heat_dicts[node][turn_node_str]
                        ):
                            map_dict[ndir].append((node, turn_node_str))

            # If we have a value for 1N
            if not np.isnan(self.heat_dicts[active_node][one_dir]):
                # If north_node[2N] is blank
                if self.is_point_in_grid(node_in_that_direction) and np.isnan(
                    self.heat_dicts[node_in_that_direction][two_dir]
                ):
                    map_dict[one_dir].append((node_in_that_direction, two_dir))
            # If we have a value for 2N
            if not np.isnan(self.heat_dicts[active_node][two_dir]):
                # If north_node[3N] is blank
                if self.is_point_in_grid(node_in_that_direction) and np.isnan(
                    self.heat_dicts[node_in_that_direction][three_dir]
                ):
                    map_dict[two_dir].append((node_in_that_direction, three_dir))
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
                    if (self.pos, new_node, new_key) in self.staging_dicts:
                        if new_len < self.staging_dicts[(self.pos, new_node, new_key)]:
                            self.staging_dicts[(self.pos, new_node, new_key)] = new_len
                    else:
                        self.staging_dicts[(self.pos, new_node, new_key)] = new_len

    def dijkstra(self):
        while not any([not np.isnan(x) for x in self.heat_dicts[(-1, -1)].values()]):
            self.update_staging()
            next_step, next_step_len = min(
                self.staging_dicts.items(), key=lambda x: x[1]
            )
            self.heat_dicts[next_step[1]][next_step[2]] = next_step_len
            self.pos = next_step[1]
            self.staging_dicts.pop(next_step)

            # active_nodes = np.where(self.active_nodes)
            # for row, col in zip(active_nodes[0], active_nodes[1]):
            #     active_node = (row, col)
            #     map_dict = self.dict_to_dict_mapping(active_node)
            #     for active_key, new_values in map_dict.items():
            #         if new_values:
            #             for new_value in new_values:
            #                 new_node = new_value[0]
            #                 new_key = new_value[1]
            #                 new_len = (
            #                     self.heat_dicts[active_node][active_key]
            #                     + self.heat_grid[new_node]
            #                 )
            #                 if (active_node, new_key) in self.staging_dicts[new_node]:
            #                     self.staging_dicts[new_node][(active_node, new_key)] = (
            #                         min(
            #                             self.staging_dicts[new_node][
            #                                 (active_node, new_key)
            #                             ],
            #                             new_len,
            #                         )
            #                     )
            #                 if new_len < next_step_len:
            #                     next_step_len = new_len
            #                     next_step = (active_node, new_node, new_key)
            # self.heat_dicts[next_step[1]][next_step[2]] = next_step_len
            # for node in next_step[:2]:
            #     self.update_active_nodes(node)

    def min_heat_loss(self):
        self.dijkstra()
        return [x for x in self.heat_dicts[-1, -1].values() if not np.isnan(x)][0] - 1


# filename = r"year_2023/tests/test_inputs/17_test_input.txt"
# m = Crucible(filename)
# m.min_heat_loss()
