from AdventOfCode.support import support
import numpy as np


class Day21:
    def __init__(self, filename):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.starting_point = tuple(np.transpose(np.where(self.file_input == "S"))[0])
        self.pos = np.zeros(self.file_input.shape, dtype=bool)
        self.pos[self.starting_point] = True
        self.nearby = support.find_nearby_coordinates(self.pos)

    def plot_grid(self):
        grid = np.zeros(self.file_input.shape, dtype=str)
        for index, value in np.ndenumerate(self.file_input):
            if value == "#":
                grid[index] = value
            elif self.pos[index]:
                grid[index] = "O"
            else:
                grid[index] = "."
        return grid

    def step(self):
        new_pos = np.zeros(self.pos.shape, dtype=bool)
        for index, value in np.ndenumerate(self.pos):
            if value:
                nearbys = self.nearby[index]
                for nearby in nearbys:
                    if self.file_input[nearby] != "#":
                        new_pos[nearby] = True
        self.pos = new_pos
        
    def steps(self, num_steps):
        for _ in range(num_steps):
            self.step()
            
    
    def count_plots(self):
        return np.sum(self.pos == True)


filename = r"year_2023/tests/test_inputs/21_test_input.txt"
m = Day21(filename)
m.plot_grid()
