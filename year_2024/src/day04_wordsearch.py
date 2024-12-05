from support import support
import numpy as np


class ClassName:
    def __init__(self, filename):
        self.list_grid = support.read_input(
            filename, flavor="str_grid", split_char=None
        )
        self.file_input = np.array(self.list_grid)

    def part1(self):
        xmas_count = 0
        it = np.nditer(self.file_input, flags=["multi_index"])
        for x in it:
            if x == "X":
                x_idx = it.multi_index
                adj_idxs = support.list_neighbors(x_idx, self.file_input, diagonal=True)
                for adj_idx in adj_idxs:
                    adj_letter = self.file_input[adj_idx]
                    if adj_letter == "M":
                        m_idx = adj_idx
                        diff_idx = support.subtract_tuples(m_idx, x_idx)
                        next_idx = support.sum_tuples(m_idx, diff_idx)
                        if not support.point_out_of_bounds(
                            next_idx[0], next_idx[1], self.list_grid
                        ):
                            next_letter = self.file_input[next_idx]
                            if next_letter == "A":
                                a_idx = next_idx
                                last_idx = support.sum_tuples(a_idx, diff_idx)
                                if not support.point_out_of_bounds(
                                    last_idx[0], last_idx[1], self.list_grid
                                ):
                                    last_letter = self.file_input[last_idx]
                                    if last_letter == "S":
                                        xmas_count += 1
        return xmas_count

    def part2(self):
        xmas_count = 0
        it = np.nditer(self.file_input, flags=["multi_index"])
        for x in it:
            if x == "A":
                a_idx = it.multi_index
                adj_idxs = support.list_neighbors(a_idx, self.file_input, diagonal=True)
                if len(adj_idxs) == 8:
                    top_left_idx = support.sum_tuples(a_idx, (-1, -1))
                    top_right_idx = support.sum_tuples(a_idx, (-1, 1))
                    bottom_left_idx = support.sum_tuples(a_idx, (1, -1))
                    bottom_right_idx = support.sum_tuples(a_idx, (1, 1))

                    top_left_letter = self.file_input[top_left_idx]
                    top_right_letter = self.file_input[top_right_idx]
                    bottom_left_letter = self.file_input[bottom_left_idx]
                    bottom_right_letter = self.file_input[bottom_right_idx]

                    if top_left_letter == "M" and bottom_right_letter == "S":
                        if top_right_letter == "M" and bottom_left_letter == "S":
                            xmas_count += 1
                        elif top_right_letter == "S" and bottom_left_letter == "M":
                            xmas_count += 1

                    elif top_left_letter == "S" and bottom_right_letter == "M":
                        if top_right_letter == "M" and bottom_left_letter == "S":
                            xmas_count += 1
                        elif top_right_letter == "S" and bottom_left_letter == "M":
                            xmas_count += 1
        return xmas_count
