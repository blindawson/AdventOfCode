from AdventOfCode.support import support
import numpy as np


class Day21:
    def __init__(self, filename, part2=False):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.starting_point = tuple(np.transpose(np.where(self.file_input == "S"))[0])
        self.file_input[self.starting_point] = "."
        self.part2 = part2
        self.pos = self.create_empty_array()
        self.pos[self.starting_point] = [(0, 0)]
        self.nearby = support.find_nearby_coordinates(self.pos)
        self.num_step = 0
        self.grid_len = self.pos.shape[0]
        self.ramp_up_steps = self.grid_len * 3
        

    def create_empty_array(self):
        arr = np.empty(self.file_input.shape, dtype=object)
        for index, _ in np.ndenumerate(arr):
            arr[index] = []
        return arr

    def plot_grid(self):
        grid = np.zeros(self.file_input.shape, dtype=str)
        for index, value in np.ndenumerate(self.file_input):
            if value == "#":
                grid[index] = value
            elif self.pos[index]:
                grid[index] = str(len(self.pos[index]))
            else:
                grid[index] = "."
        return grid

    def step(self):
        new_pos = self.create_empty_array()
        for index, value in np.ndenumerate(self.pos):
            if value:
                if self.part2:
                    y, x = index
                    nearbys = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
                else:
                    nearbys = self.nearby[index]
                for nearby in nearbys:
                    update_value = value
                    y, x = nearby
                    if nearby[0] < 0:
                        nearby = (self.grid_len - 1, nearby[1])
                        update_value = [(v[0] - 1, v[1]) for v in value]
                    elif nearby[0] == self.grid_len:
                        nearby = (0, nearby[1])
                        update_value = [(v[0] + 1, v[1]) for v in value]
                    elif nearby[1] < 0:
                        nearby = (nearby[0], self.grid_len - 1)
                        update_value = [(v[0], v[1] - 1) for v in value]
                    elif nearby[1] == self.grid_len:
                        nearby = (nearby[0], 0)
                        update_value = [(v[0], v[1] + 1) for v in value]

                    if self.file_input[nearby] != "#":
                        new_pos[nearby] = list(set(new_pos[nearby] + update_value))
        self.pos = new_pos

    def steps(self, num_steps):
        plots = []
        start_step = self.num_step
        for _ in range(num_steps):
            self.step()
            plots.append(self.count_plots())
            self.num_step += 1
        end_step = self.num_step
        step_range = np.arange(start_step + 1, end_step + 1)
        return step_range, np.array(plots)

    def count_plots(self):
        return np.sum(np.vectorize(len)(self.pos))

    def extrapolate_steps(self, target_step, ceof_deg=2):
        _, _ = self.steps(self.grid_len * 3)
        x, y = self.steps(self.grid_len * 8)
        target_mod = target_step % self.grid_len
        mod_idxs = [idx for idx in range(len(x)) if x[idx] % self.grid_len == target_mod]
        coefficients = np.polyfit(x[mod_idxs], y[mod_idxs], ceof_deg)

        return round(np.polyval(coefficients, target_step))

    def reset(self):
        self.pos = self.create_empty_array()
        self.pos[self.starting_point] = [(0, 0)]
        self.num_step = 0

