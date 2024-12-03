from support import support
import pandas as pd


class ClassName:
    def __init__(self, filename):
        self.file_input = pd.DataFrame(
            support.read_input(filename, flavor="split_int", split_char="   ")
        )

        self.list1 = self.file_input[0].sort_values(ignore_index=True)
        self.list2 = self.file_input[1].sort_values(ignore_index=True)
        self.dist = (self.list1 - self.list2).abs()

        self.list1_ct = self.list1.value_counts()
        self.list2_ct = self.list2.value_counts()

    def part1(self):
        return self.dist.sum()

    def part2(self):
        sum_dist = 0
        for idx, value in self.list1_ct.items():
            if idx in self.list2_ct.index:
                sum_dist += idx * value * self.list2_ct[idx]
        return sum_dist
