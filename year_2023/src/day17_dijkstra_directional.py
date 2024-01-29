from AdventOfCode.support import support
import numpy as np


class Crucible:
    def __init__(self, filename):
        self.heat_grid = np.array(support.read_input(filename, flavor="int_grid"))
        self.pos = (0, 0)
        self.heat_dicts = np.empty(self.heat_grid.shape, dtype=dict)
        self.active_nodes = np.zeros(self.heat_grid.shape, dtype=bool)
        self.active_nodes[self.pos] = True
        self.empty_dict = {
            "1N": np.nan,
            "2N": np.nan,
            "3N": np.nan,
            "1E": np.nan,
            "2E": np.nan,
            "3E": np.nan,
            "1S": np.nan,
            "2S": np.nan,
            "3S": np.nan,
            "1W": np.nan,
            "2W": np.nan,
            "3W": np.nan,
        }
        self.heat_dicts[self.pos] = self.empty_dict.copy()
        self.heat_dicts[self.pos]["3E"] = 0
        self.heat_dicts[self.pos]["3S"] = 0

    def what_direction_did_we_move(self, pos1, pos2):
        pos_diff = support.subtract_tuples(pos2, pos1)
        for key, value in support.direction_dict.items():
            if pos_diff == value:
                return key

    def update_heat_dict(self, pos1, pos2):
        move_direction = self.what_direction_did_we_move(pos1, pos2)
        if move_direction == "S":
            for key, value in self.heat_dicts[pos1].items():
                if (key[1] == "W") or (key[1] == "E"):
                    self.heat_dicts[pos2]["1S"] = np.nanmin(
                        [self.heat_dicts[pos2]["1S"], value + self.heat_grid[pos2]]
                    )
                elif key == "1S":
                    self.heat_dicts[pos2]["2S"] = np.nanmin(
                        [self.heat_dicts[pos2]["2S"], value + self.heat_grid[pos2]]
                    )
                elif key == "2S":
                    self.heat_dicts[pos2]["3S"] = np.nanmin(
                        [self.heat_dicts[pos2]["3S"], value + self.heat_grid[pos2]]
                    )
                

    def dijkstra_step(self):
        true_indices_2d = np.where(self.active_nodes)
        for row, col in zip(true_indices_2d[0], true_indices_2d[1]):
            active_node = (row, col)
            for adjacent_node in support.list_neighbors(active_node, self.heat_grid):
                if not self.heat_dicts[adjacent_node]:
                    self.heat_dicts[adjacent_node] = self.empty_dict.copy()


filename = r"year_2023/tests/test_inputs/17_test_input.txt"
m = Crucible(filename)
m.heat_grid

m.heat_dicts[(1,0)] = m.empty_dict.copy()
m.update_heat_dict((0,0), (1,0))
m.heat_dicts[(1,0)]