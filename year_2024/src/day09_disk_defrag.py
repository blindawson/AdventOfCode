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

        self.blocks = pd.DataFrame(columns=["ID", "Range", "Size", "Moved"])
        self.blocks.set_index("ID", inplace=True)

        self.gaps = pd.DataFrame(columns=["Range", "Size"])

    def create_block(self, id, idx_range):
        self.blocks.loc[id] = {
            "Range": idx_range,
            "Size": len(idx_range),
            "Moved": False,
        }

    def create_gap(self, idx_range):
        new_gap = pd.DataFrame({"Range": [idx_range], "Size": [len(idx_range)]})
        self.gaps = pd.concat([self.gaps, new_gap], ignore_index=True)

    def part2(self):
        block_id = 0
        input_idx = 0
        output_idx = 0
        while input_idx < self.disk_len:
            block_size = int(self.disk_input[input_idx])
            self.create_block(block_id, [output_idx + i for i in range(block_size)])
            input_idx += 1
            output_idx += block_size
            block_id += 1

            if input_idx < self.disk_len:
                block_size = int(self.disk_input[input_idx])
                self.create_gap([output_idx + i for i in range(block_size)])
                input_idx += 1
                output_idx += block_size

        # for blocks from last to first
        for block_idx, block in self.blocks.iloc[::-1].iterrows():
            print(block_idx)
            if not block["Moved"]:
                for gap_idx, gap in self.gaps.iterrows():
                    if (
                        block["Size"] <= gap["Size"]
                        and block["Range"][0] > gap["Range"][0]
                    ):
                        self.blocks.at[block_idx, "Range"] = [
                            gap["Range"][0] + i for i in range(block["Size"])
                        ]
                        self.gaps.loc[gap_idx, "Size"] = gap["Size"] - block["Size"]
                        self.gaps.at[gap_idx, "Range"] = [
                            self.blocks.at[block_idx, "Range"][-1] + 1 + i
                            for i in range(gap["Size"] - block["Size"])
                        ]
                        break
                self.blocks.loc[block_idx, "Moved"] = True
        
        checksum = 0
        for block_idx, block in self.blocks.iterrows():
            checksum += block_idx * sum(block["Range"])
            
        return checksum


filename = r"year_2024/tests/test_inputs/09_test_input.txt"
filename = r"year_2024/input/09_disk_defrag.txt"
m = Part2(filename)
# m.part2()
