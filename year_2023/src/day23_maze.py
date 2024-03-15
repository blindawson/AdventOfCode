from AdventOfCode.support import support
import numpy as np


class Maze:
    def __init__(self, filename, part2=False):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.start_yx = (0, 1)
        self.end_yx = (self.file_input.shape[0] - 1, self.file_input.shape[1] - 2)
        self.explored = np.zeros(self.file_input.shape, dtype=int)
        if part2:
            self.file_input = np.char.replace(self.file_input, ">", ".")
            self.file_input = np.char.replace(self.file_input, "<", ".")
            self.file_input = np.char.replace(self.file_input, "^", ".")
            self.file_input = np.char.replace(self.file_input, "v", ".")

    def follow_path(self, yx, explored):
        explored[yx] = 1
        adjs = self.search_adjacent(yx, explored)
        while len(adjs) == 1:
            yx = adjs[0]
            explored[yx] = 1
            adjs = self.search_adjacent(yx, explored)

        new_explores = []
        for adj in adjs:
            # print(len(adjs))
            new_map = self.follow_path(adj, explored.copy())
            if new_map[self.end_yx]:
                print(new_map.sum())
                new_explores.append(new_map)
        if new_explores:
            sums = [np.sum(x) for x in new_explores]
            max_index = np.argmax(sums)
            explored = new_explores[max_index]
        return explored

    def search_adjacent(self, yx, explored):
        adjs1 = support.list_neighbors(yx, self.file_input)
        adjs2 = []
        for adj in adjs1:
            adj_char = self.file_input[adj]
            if explored[adj]:
                continue
            elif adj_char == "#":
                continue
            elif adj_char == ".":
                adjs2.append(adj)
            elif adj_char == ">":
                if support.subtract_tuples(adj, yx) == (0, 1):
                    adjs2.append(adj)
            elif adj_char == "<":
                if support.subtract_tuples(adj, yx) == (0, -1):
                    adjs2.append(adj)
            elif adj_char == "^":
                if support.subtract_tuples(adj, yx) == (-1, 0):
                    adjs2.append(adj)
            elif adj_char == "v":
                if support.subtract_tuples(adj, yx) == (1, 0):
                    adjs2.append(adj)
        return adjs2


# filename = r"year_2023/tests/test_inputs/23_test_input.txt"
filename = r"year_2023/input/23_maze.txt"

m = Maze(filename, part2=True)
m.follow_path((0, 1), m.explored.copy()).sum() - 1
