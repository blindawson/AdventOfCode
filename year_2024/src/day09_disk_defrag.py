from support import support
import math
import pandas as pd


class Part1:
    def __init__(self, filename):
        self.disk_input = support.read_input(filename)[0]
        self.disk_len = len(self.disk_input)

        self.move_left_block(reset=True)
        self.move_right_block(reset=True)

        self.placement_idx = 0
        self.checksum = 0

    def move_left_block(self, reset=False, hold_id=False):
        if reset:
            self.left_idx = 0
            self.left_block_id = 0
        else:
            self.left_idx += 1
            self.left_block_id += 1
        self.left_block_size = int(self.disk_input[self.left_idx])
        self.left_remainder = self.left_block_size
        if hold_id:
            self.left_block_id -= 1

    def move_right_block(self, reset=False):
        if reset:
            self.right_idx = self.disk_len - 1
            self.right_block_id = math.floor(self.disk_len / 2)
        else:
            self.right_idx -= 2
            self.right_block_id -= 1
        self.right_block_size = int(self.disk_input[self.right_idx])
        self.right_remainder = self.right_block_size

    def add_to_checksum(self, block_size, block_id):
        placement_idxs = range(self.placement_idx, self.placement_idx + block_size)
        self.checksum += sum(placement_idxs) * block_id
        self.placement_idx += block_size

    def part1(self):
        while self.left_block_id <= self.right_block_id:
            self.add_to_checksum(self.left_remainder, self.left_block_id)
            self.move_left_block()

            while self.left_block_id <= self.right_block_id:
                if self.left_block_id == self.right_block_id:
                    self.move_left_block(hold_id=True)
                    self.left_remainder = self.right_remainder
                    break
                moving_size = min(self.left_remainder, self.right_remainder)
                self.add_to_checksum(moving_size, self.right_block_id)
                self.left_remainder -= moving_size
                self.right_remainder -= moving_size

                # if part of left gap remains then move right block and repeat
                if self.left_remainder:
                    self.move_right_block()
                # if part of right block remains then move left block and break
                elif self.right_remainder:
                    self.move_left_block(hold_id=True)
                    break
                else:
                    self.move_left_block(hold_id=True)
                    self.move_right_block()
                    break
        return self.checksum


class Part2:
    def __init__(self, filename):
        self.disk_input = support.read_input(filename)[0]
        self.disk_len = len(self.disk_input)

        block_sizes = [int(x) for x in self.disk_input[::2]]
        self.blocks = pd.DataFrame(
            {
                "ID": range(len(block_sizes)),
                "Range": [[]] * len(block_sizes),
                "Size": block_sizes,
            }
        )
        self.blocks.set_index("ID", inplace=True)

        gap_sizes = [int(x) for x in self.disk_input[1::2]]
        self.gaps = pd.DataFrame(
            {
                "ID": range(len(gap_sizes)),
                "Range": [[]] * len(gap_sizes),
                "Size": gap_sizes,
            }
        )
        self.gaps.set_index("ID", inplace=True)

        previous_gap_loc = -1
        for idx in range(max(self.blocks.index[-1], self.gaps.index[-1]) + 1):
            block_range = [
                previous_gap_loc + 1 + x for x in range(self.blocks.loc[idx, "Size"])
            ]
            self.blocks.at[idx, "Range"] = block_range
            if block_range:
                previous_block_loc = block_range[-1]
            else:
                previous_block_loc = previous_gap_loc

            if idx <= self.gaps.index[-1]:
                gap_range = [
                    previous_block_loc + 1 + x
                    for x in range(self.gaps.loc[idx, "Size"])
                ]
                self.gaps.at[idx, "Range"] = gap_range
                if gap_range:
                    previous_gap_loc = gap_range[-1]
                else:
                    previous_gap_loc = previous_block_loc

    def part2(self):
        mask_dict = {key: self.gaps["Size"] >= key for key in range(10)}
        update_dict = {}
        for block_idx, block in self.blocks.iloc[::-1].iterrows():
            if block["Size"] > 0:
                print(self.blocks, self.gaps, update_dict)
                large_gaps = mask_dict[block["Size"]]
                # large_gaps = self.gaps[self.gaps["Size"] >= block["Size"]]
                if not self.gaps[large_gaps].empty:
                    gap = self.gaps[large_gaps].iloc[0]
                    gap_idx = gap.name
                    if gap_idx < block_idx:

                        update_dict[block_idx] = [
                            gap["Range"][0] + i for i in range(block["Size"])
                        ]

                        new_gap_size = gap["Size"] - block["Size"]
                        for size in range(gap["Size"], new_gap_size, -1):
                            mask_dict[size][gap_idx] = False
                        self.gaps.loc[gap_idx, "Size"] = new_gap_size

                        if new_gap_size == 0:
                            self.gaps.at[gap_idx, "Range"] = []
                        else:
                            self.gaps.at[gap_idx, "Range"] = gap["Range"][
                                -new_gap_size:
                            ]

        update_series = pd.Series(update_dict)
        self.blocks.loc[update_series.index, "Range"] = update_series.values

        checksum = 0
        print(self.blocks, self.gaps, update_dict)
        for block_idx, block in self.blocks.iterrows():
            checksum += block_idx * sum(block["Range"])

        return checksum
