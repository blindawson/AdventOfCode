from AdventOfCode.support import support
import numpy as np


class Scratchcards:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.sum_points = 0
        self.matches_list = []
        for r in self.file_input:
            matches = self.calc_matches(r)
            self.matches_list.append(matches)
            self.sum_points += int(2 ** (matches - 1))
        self.card_count = np.ones(len(self.file_input), dtype=int)
        for index, item in enumerate(self.matches_list):
            self.card_count[index + 1 : index + item + 1] += self.card_count[index]

    def calc_matches(self, row):
        # card_num = row[1][:-1]
        split_index = row.index("|")
        winning_nums = [x for x in row[2 : split_index + 1] if x.isnumeric()]
        have_nums = [x for x in row[split_index + 1 :] if x.isnumeric()]
        matches = len([x for x in have_nums if x in winning_nums])
        return matches
